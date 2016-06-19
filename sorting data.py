#Group 6 
# Programming pair - Shirly and siddhesh 

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

sorting(gedcom_file)