import sys  
from datetime import datetime
from datetime import timedelta

#Dictionary of the family
fam ={}
#Dictionary of the individual
indi ={}

#getting todays date 
today = datetime.now()

date_type = ''

print "Please enter file path only"
ged_file = raw_input ("Enter the file name:")

#Usng try and except to print error message if file not found

try:
    open_file = open ( ged_file )

except:
    print "File not found"
    raise SystemExit

for line in open_file:
        line = line.rstrip().lstrip()
        #spliting line into individual words
        words = line.split()
        
        #pushing individual data
        if words[0] == '0' and len(words) == 3 and words[2] == 'INDI':
            id_type = words[1]
            id_tag = words[2]
            indi[id_type] = {}
        
        elif words[0] == '1' and len(words) >3 and words[1] == 'NAME':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        elif words[0] == '1' and len(words) ==3 and words[1] == 'SEX':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        elif words[0] == '1' and len(words) == 2 and words[1] == 'BIRT':
            ex1 = next(open_file).rstrip().lstrip()
            term1 = ex1.split()
            indi[id_type]['BIRT'] = ' '.join(term1[2:])
            
        elif words[0] == '1' and len(words) == 3 and words[1] == 'DEAT':
            ex2 = next(open_file).rstrip().lstrip()
            term2 = ex2.split()
            indi[id_type]['DEAT'] = ' '.join(term2[2:])
    
        elif words[0] == '1' and len(words) == 3 and words[1] == 'FAMS':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        elif words[0] == '1' and len(words) == 3 and words[1] == 'FAMC':
            indi[id_type][words[1]] = ' '.join(words[2:])
 
        #pushing family data
        if words[0] == '0' and len(words) == 3 and words[2] == 'FAM':
            id_type1 = words[1]
            id_tag1 = words[2]
            fam[id_type1] = {}
            fam[id_type1]['CHIL'] = []
        
        elif words[0] == '1' and len(words) == 3 and words[1] == 'HUSB':
            fam[id_type1][words[1]] = ' '.join(words[2:])
            
        elif words[0] == '1' and len(words) == 3 and words[1] == 'WIFE':
            fam[id_type1][words[1]] = ' '.join(words[2:])
            
        elif words[0] == '1' and len(words) == 3 and words[1] == 'CHIL':
            fam[id_type1][words[1]] += [' '.join(words[2:])]
        
        elif words[0] == '1' and len(words) == 2 and words[1] == 'MARR':
            ex3 = next(open_file).rstrip().lstrip()
            term3 = ex3.split()
            fam[id_type1]['MARR'] = ' '.join(term3[2:])
        
        elif words[0] == '1' and len(words) == 2 and words[1] == 'DIV':
            ex4 = next(open_file).rstrip().lstrip()
            term4 = ex4.split()
            fam[id_type1]['DIV'] = ' '.join(term4[2:])

print indi
print "\n"
print fam
print "\n"
print "The current date is:-",today
print "\n"

#-------------------------------------------------------------------------------start - US03 -birth before death
#Programmer - Siddhesh Palav
print "Extracting records from individual dictionary that has birth and death associated with individual"
print "\n"

for individual_id in indi:
    individual = indi[individual_id]
    if individual.has_key('BIRT') and individual.has_key('DEAT'):
        
        Bdate = indi[individual_id]["BIRT"]
        Ddate = indi[individual_id]["DEAT"]
        
        currentyear_BD =datetime.strptime(Bdate,"%d %b %Y")
        currentyear_DD =datetime.strptime(Ddate,"%d %b %Y")
        
        print "current year Birth Date",currentyear_BD
        print "current year Death Date",currentyear_DD
        
        if currentyear_BD > currentyear_DD:
            print "Birth is occured after the death of",individual["NAME"]
            print"\n"
        else:
            print "Birth is occured before the death of",individual["NAME"]
            print"\n"
     
#-------------------------------------------------------------------------------end - US03 -birth before death  

#-------------------------------------------------------------------------------Start-US02 Birth before marriage     
#Programmer - Siddhesh Palav
for fam_id in fam:
    famdata = fam[fam_id]
    
    HID = ""
    WID = ""
    weddate = ""
    divdate = ""
    if famdata .has_key('HUSB'): HID = famdata ['HUSB']
    if famdata .has_key('WIFE'): WID = famdata ['WIFE']
    if famdata .has_key('MARR'): weddate = famdata ['MARR']
    if famdata .has_key('DIV'): divdate = famdata ['DIV']
  
    if HID and WID and weddate:
        WD =datetime.strptime(weddate,"%d %b %Y")

        HB = datetime.strptime(indi[HID]['BIRT'],"%d %b %Y")
        
        WB = datetime.strptime(indi[WID]['BIRT'],"%d %b %Y")
        
        if HB < WD:
            print "Birth happened before marraiage of",indi[HID]["NAME"]
        else:
            print "marraige happened beore Birth of",indi[HID]["NAME"]

        if WB < WD:
            print "Birth happened before marraiage of",indi[WID]["NAME"]
        else:
            print "marraige happened beore Birth of",indi[WID]["NAME"]
        
        print "\n"

#-------------------------------------------------------------------------------End -US02 Birth before marriage

#-------------------------------------------------------------------------------US04 start-Marriage before divorce
#programmer - Shirly Rabindran
for fam_id in fam:
    famdata = fam[fam_id]
    
    HID = ""
    WID = ""
    weddate = ""
    divdate = ""
    if famdata .has_key('HUSB'): HID = famdata ['HUSB']
    if famdata .has_key('WIFE'): WID = famdata ['WIFE']
    if famdata .has_key('MARR'): weddate = famdata ['MARR']
    if famdata .has_key('DIV'): divdate = famdata ['DIV']
    if weddate != "" and divdate != "":
        print "collecting all the family wedding date and divorce date"
        print "Couple is, Husband:-",indi[HID]["NAME"],"Wife:-",indi[WID]["NAME"]
        if weddate > divdate:
            print "The Wedding date is before Divorce date"
            print "\n"
        else:
            print "The Wedding date is after the Divorce date"
            print "\n"
            
#-------------------------------------------------------------------------------US04 end-Marriage before divorce

#-------------------------------------------------------------------------------US23-start -Unique name and birthdate
#programmer - Shirly Rabindran

Namelist =[]
Namelist1 =[]
Birthdate =[]
Birthdate1 =[]

for individual_id in indi:
    individual = indi[individual_id]
    
    #if individual.has_key('BIRT'):
    Name = indi[individual_id]["NAME"].split()
    Namelist.append(Name[0])
    Bdate = indi[individual_id]["BIRT"]
    Birthdate.append(Bdate)

print "Total number of names:-",len(Namelist)
Namelist1 = set (Namelist)
print "Number of duplicate names:-",len(Namelist)-len(Namelist1)

#Sorting and printing duplicates
Namelist.sort()
for i in range(0,len(Namelist)-1):
               if Namelist[i] == Namelist[i+1]:
                   print "Name",str(Namelist[i]) + " is duplicate"
print "\n"

print "Total number of Birthdates:-",len(Birthdate)
Birthdate1  = set (Birthdate)
print "Number of duplicate names:-",len(Birthdate) - len(Birthdate1)

Birthdate.sort()
for j in range(0,len(Birthdate)-1):
               if Birthdate[j] == Birthdate[j+1]:
                   print "Bithdate",str(Birthdate[j]) + " is duplicate"
#-------------------------------------------------------------------------------US23-End-Unique name and birthdate