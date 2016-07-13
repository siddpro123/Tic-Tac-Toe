import sys 
import pandas as pd 
from datetime import datetime
from datetime import timedelta

#Dictionary of the family
fam ={}
#Dictionary of the individual
indi ={}

#getting todays date 
today = datetime.now()
end_date1 =  today - timedelta(days=30)
end_date2 =  today + timedelta(days=30)


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
print "\n"

print"===================================== INDIVIDUAL INFORMATION ==================================================="
#printing individual data in tabular form
person = pd.DataFrame(indi).T
person.fillna(0, inplace=True)
print(person)

print "\n"

print"===================================== FAMILY INFORMATION ========================================================"
#printing family data in tabular form
Family = pd.DataFrame(fam).T
Family.fillna(0, inplace=True)
print(Family)
print "\n"

#======================================== US35 Start-List recent birth =================================================
#Programmer - Shirly Rabindran
#Birth is normal thing hence we are not considering it as an anomaly or an error
for individual_id in indi:
    individual = indi[individual_id] 
    
    if individual.has_key('BIRT'):       
       Birthdate = datetime.strptime(indi[individual_id]["BIRT"],"%d %b %Y")
       if Birthdate >= end_date1 and Birthdate <= today:
           print "(US35) - ID:-",individual_id,",Name:-",individual["NAME"], "is born within last 30 days and has birthdate :-",Birthdate,"\n" 

#===================================== US35 End-List recent birth  ======================================================
for family_id in fam:
    family = fam[family_id]

    husbandID = ""
    wifeID = ""
    weddingDate = ""
    divorceDate = ""
    if family.has_key('HUSB'): husbandID = family['HUSB']
    if family.has_key('WIFE'): wifeID = family['WIFE']
    if family.has_key('MARR'): weddingDate = family['MARR']
    if family.has_key('DIV'): divorceDate = family['DIV']

#===================================== US05 Start-Marriage before death ==================================================
#Programmer - Siddhesh Palav

    if husbandID and wifeID and weddingDate:
        WedDate = datetime.strptime(weddingDate,"%d %b %Y")
        
        if indi[husbandID].has_key("DEAT"):
            HusbandDeath = datetime.strptime(indi[husbandID]['DEAT'],"%d %b %Y")
            if HusbandDeath < WedDate:
                print "Family ID:-'",family_id,indi[husbandID]["NAME"],"(Husband) and",indi[wifeID]["NAME"],"(Wife) married on",WedDate
                print "Error(US05) - Husband",indi[husbandID]["NAME"],"died before Marraiage \n"

        if indi[wifeID].has_key("DEAT"):
            WifeDeath = datetime.strptime(indi[wifeID]['DEAT'],"%d %b %Y")
            if WifeDeath < WedDate:
                print "Family ID:-'",family_id,indi[husbandID]["NAME"],"(Husband) and",indi[wifeID]["NAME"],"(Wife) married on",WedDate
                print "Error(US05) - Wife",indi[wifeID]["NAME"],"died before Marraiage \n"

#===================================== US05 End-Marriage before death ======================================================

#======================================== US21 Start- Correct gender for role ============================================== 
#Programmer - Siddhesh Palav
    if indi[husbandID]['SEX'] != "M":
        print "checking 'HUSB' tag and corresponding sex should be Male/'M'"
        print "Error(US21) - ID:-",individual_id,"Name",indi[husbandID]["NAME"],"has sex '",indi[husbandID]['SEX'],"' and hence should play a role of Wife \n"

    if indi[wifeID]['SEX'] != "F":
        print "checking 'WIFE' tag and corresponding sex should be Female/'F'"
        print "Error(US21) - ID:- ",individual_id,",Name:-",indi[wifeID]["NAME"],"has sex '",indi[wifeID]['SEX'],"' and hence should play a role of Husband \n"

#======================================== US21 End- Correct gender for role ================================================== 

#===================================== US39 Start -List upcoming anniversaries ===============================================
#Programmer - Shirly Rabindran
#Checking for Aniversary date is very normal and hence we are not considering it as an anomaly or an error
    if husbandID and wifeID and weddingDate:
        WedDate2 = datetime.strptime(weddingDate,"%d %b %Y").replace(year =today.year)
        if WedDate2 >= today and WedDate2 <= end_date2:
            print "Family ID:-'",family_id,indi[husbandID]["NAME"],"(Husband) and",indi[wifeID]["NAME"],"(Wife) married on",WedDate,",Their aniversary is within 30 days \n"

#===================================== US39 End -List upcoming anniversaries =================================================
