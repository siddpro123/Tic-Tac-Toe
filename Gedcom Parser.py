import sys  # graceful exit
from datetime import datetime
from datetime import timedelta

fam ={}
indi ={}

today = datetime.now()

date_type = ''
tags =["INDI","NAME", "SEX","BIRT", "DATE","DEAT","DATE","FAM", "FAMC", "FAMS"]

# open and read GEDCOM file so that i dont have to keep entering file name everytime during testing 
fname = open('C:\Users\shree\Canopy\My-Family-19-Jun-2016-672.ged')

for line in fname:
        line = line.rstrip().lstrip()
        words = line.split()
        if words[0] == '0' and len(words) == 3 and words[2] == 'INDI':
            id_type = words[1]
            id_tag = words[2]
            indi[id_type] = {}
        
        elif words[0] == '1' and len(words) >3 and words[1] == 'NAME':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        elif words[0] == '1' and len(words) ==3 and words[1] == 'SEX':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        #adding date - problem area 
        elif words[0] == '1' and len(words) == 2 and words[1] == 'BIRT':
            ex1 = next(fname).rstrip().lstrip()
            term1 = ex1.split()
            indi[id_type]['BIRT'] = ' '.join(term1[2:])
            
        
        elif words[0] == '1' and len(words) == 3 and words[1] == 'DEAT':
            ex2 = next(fname).rstrip().lstrip()
            term2 = ex2.split()
            indi[id_type]['DEAT'] = ' '.join(term2[2:])
    
        elif words[0] == '1' and len(words) == 3 and words[1] == 'FAMS':
            indi[id_type][words[1]] = ' '.join(words[2:])
        
        elif words[0] == '1' and len(words) == 3 and words[1] == 'FAMC':
            indi[id_type][words[1]] = ' '.join(words[2:])
 
        
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
            ex3 = next(fname).rstrip().lstrip()
            term3 = ex3.split()
            fam[id_type1]['MARR'] = ' '.join(term3[2:])
        
        elif words[0] == '1' and len(words) == 2 and words[1] == 'DIV':
            ex4 = next(fname).rstrip().lstrip()
            term4 = ex4.split()
            fam[id_type1]['DIV'] = ' '.join(term4[2:])
print indi
print "\n"
print fam
print today

'''
for individual_id in sorted(indi.keys()):
    print "Individual ID:", individual_id
    print "Name:", indi[individual_id]["NAME"]
    if indi[individual_id].has_key('BIRT'):
        print "Birth:", indi[individual_id]["BIRT"],"\n"
'''


for individual_id in indi:
    individual = indi[individual_id]
    
    
#-------------------------------------------------------------------------------start - US03 -birth before death
    if individual.has_key('BIRT') and individual.has_key('DEAT'):
        Bdate = indi[individual_id]["BIRT"]
        Ddate = indi[individual_id]["DEAT"]
        currentyear_BD =datetime.strptime(Bdate,"%d %b %Y")
        currentyear_DD =datetime.strptime(Ddate,"%d %b %Y")
        print "current year BD",currentyear_BD
        print "current year DD",currentyear_DD
        
        if currentyear_BD > currentyear_DD:
            print "Error -  Birth is occured after the death of",individual["NAME"]
        else:
            print "Error -  Birth is occured before the death of",individual["NAME"]
      
#-------------------------------------------------------------------------------end - US03 -birth before death  

       
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
            
#-------------------------------------------------------------------------------start - US02 Birth before marriage

    if husbandID and wifeID and weddingDate:
        WD =datetime.strptime(weddingDate,"%d %b %Y")

        HB = datetime.strptime(indi[husbandID]['BIRT'],"%d %b %Y")
        
        WB = datetime.strptime(indi[wifeID]['BIRT'],"%d %b %Y")

        if HB < WD:
            print "Birth happened before marraiage of",indi[husbandID]["NAME"]
        else:
            print "marraige happened beore Birth of",indi[husbandID]["NAME"]

        if WB < WD:
            print "Birth happened before marraiage of",indi[wifeID]["NAME"]
        else:
            print "marraige happened beore Birth of",indi[wifeID]["NAME"]
        
        print "\n"

#-------------------------------------------------------------------------------End -US02 Birth before marriage










      