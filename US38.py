#Group 06
#Programmer - Siddhesh palav
#Group 6
#program devloped by - Siddhesh palav
#this program is appended to the main sprint1 program

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