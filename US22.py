#Group 6
#program devloped by - Siddhesh palav
#this program is appended to the main sprint1 program

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