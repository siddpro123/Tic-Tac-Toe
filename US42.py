#Group 6
#program devloped by - Shirly Rabindran
#this program is appended to the main sprint1 program

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