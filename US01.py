#Group 6
#program devloped by - Shirly rabindran
#this program is appended to the main sprint1 program

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