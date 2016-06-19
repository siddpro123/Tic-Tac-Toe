import re
from datetime import datetime
from datetime import timedelta

VALID_TAGS = ('INDI', 'NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'FAM', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE')

gedcom_file = open ('C:\Users\shree\Canopy\My-Family-18-Jun-2016-986.ged')

#storing individual and family data into the list
def sorting(file):

    Indidata = []
    FAMdata = []


    print("Reading from gedcom file:-", gedcom_file)

    # save INDI/FAMC at level 0 lines
    prev_tag = ""

    #looping through file lines
    for line in gedcom_file:

        levelnumber = None
        tagname = None
        arg = None

    #extracting data
        if line.startswith('0 @'):
            levelumber, arg, tagname = re.match('([012])\s+([\@\w]+)\s+(.*?)$', line).groups()
            prev_tag = tagname
        else:
            levelnumber, tagname, arg = re.match('([012])\s+(\w+)\s+(.*?)$', line).groups()

        person = dict()
        family = dict()
    
    #storing individual data according to family and individual    
        if prev_tag == 'INDI':
            person['levelnumber'] = levelnumber
            person['tagname'] = tagname
            person['arg'] = arg
            Indidata.append(person)

        if prev_tag == 'FAM' :
            family['levelnumber'] = levelnumber
            family['tagname'] = tagname
            family['arg'] = arg
            FAMdata.append(family) 
        

#--------------------------------------------------------------------------------starting user story 22 - Unique ID
    indi_id = []
    fam_id = []
    
    for index,i in enumerate(FAMdata):
        tag = i['tagname'] 
        arg = i['arg']
        if tag == 'FAM':
    	   fam_id.append(arg)

    	
    for index,i in enumerate(Indidata):
        tag = i['tagname'] 
        arg = i['arg'] 

        if tag == 'INDI':
            indi_id.append(arg)
            
        
    length1 = len(indi_id)
    print "length of the list containing INDI id before checking for duplicate:-",length1
    indi_id = set(indi_id)
    length2 = len(indi_id)
    print "length of list containing INDI id after checking for duplicate",length2
    
    print "\n"
    
    length3 = len(fam_id)
    print "length of the list containing FAM id before checking for duplicate:-",length3
    fam_id = set(fam_id)
    length4 = len(fam_id)
    print "length of the containing INDI id after checking for duplicate",length4
#--------------------------------------------------------------------------------end of user story 22

#--------------------------------------------------------------------------------starting of user story 38  list upcoming birthday 
    present = datetime.now()
    print (present)
   
    indi = dict()
    for index,i in enumerate(Indidata):
        tagname = i['tagname'] 
        arg = i['arg'] 
    # memorize ID
        if tagname == 'INDI':
            indi_id = arg
            indi[indi_id] = dict()
        elif tagname == 'BIRT':
            indi[indi_id]["BIRT"] = datetime.strptime(Indidata[index + 1]['arg'], "%d %b %Y").replace(year =present.year)
             #indi[indi_id]["BIRT"].replace(year =present.year)
        elif tagname == 'DEAT':
            indi[indi_id]["DEAT"] = True
        elif tagname == 'NAME':
            indi[indi_id]["NAME"]= arg

    for key in indi.keys():
        if "DEAT" in indi.keys():
            continue
        elif indi[key]["BIRT"] > datetime.now():
            if indi[key]["BIRT"] < (datetime.today() + timedelta(days=30)):
                print indi[key]["NAME"],",your birthday is within next 30 days"
                print "\n"
            else:
                print indi[key]["NAME"],",your birthday is not within next 30 days"
                print "\n"
# -------------------------------------------------------------------------------end of user story 38 
    personDates = dict() # stores deat/birth dates
    familyDates = dict()
    id = '' # remembers ID to link dates back to individual 
  
    # extract MARR and DIVO date from families
    for index,i in enumerate(FAMdata):
        tagname  = i['tagname'] 
        arg = i['arg']
    
    # memorize ID
        if tagname == 'FAM':
            id = arg
            familyDates[id] = dict()
        
        if tagname == 'DATE':
            date_string = arg
            familyDates[id][tagname] = datetime.strptime(date_string, "%d %b %Y")
            Famdate =familyDates[id][tagname]
            
            if Famdate >= present:
               print ('US01 Only dates before current date allowed')
               print ('Marriage/Divorce recorded in the Gedcom file should be prior to today')
               print ('>>Error for',id,'with marriage/divorce date',Famdate)
               print "\n"

#--------------------------------------------------------------------------------starting of user story 01  
  # extract BIRTH and DEAT dates from individuals
    for index,i in enumerate(Indidata):
        tag = i['tagname'] 
        arg = i['arg'] 
   
    # memorize ID
        if tag == 'INDI':
            id = arg
            personDates[id] = dict()

        if tag == 'DATE':
            date_string = arg
            personDates[id][tag] = datetime.strptime(date_string, "%d %b %Y")
            Indidate = personDates[id][tag]
  
  #See if there are dates post the current date/including current date  
  
            if Indidate >= present:
                print ('US01 Only dates before current date allowed')
                print ('Birth/Death recorded in the Gedcom file should be prior to today')
                print ('>>Error for',id,'with birth/death date',Indidate)
                print "\n"
#--------------------------------------------------------------------------------end of user story 1

#--------------------------------------------------------------------------------start of user story 42 reject i
    indi = dict()
    for index,i in enumerate(Indidata):
        tagname = i['tagname'] 
        arg = i['arg'] 
    # memorize ID
        if tagname == 'INDI':
            indi_id = arg
            indi[indi_id] = dict()
        elif tagname == 'BIRT':
            indi[indi_id]["BIRT"] = datetime.strptime(Indidata[index + 1]['arg'], "%d %b %Y")
        elif tagname == 'NAME':
            indi[indi_id]["NAME"]= arg
    
    now = datetime.now()
    
    for key in indi.keys():
  	if indi[key]["BIRT"].year > now.year:
  		print("US42 ERROR Reject illegitimate dates")
                print("Illegitimate date is:-" ,indi[key])
                print "\n"
#--------------------------------------------------------------------------------end of user story 42 reject i
sorting(gedcom_file)
