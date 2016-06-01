#Practice programming with GEDCOM data Assignment:
#programer - Siddhesh Palav
#Prof. Rowland
# asking user to input file name/ address.

#creating list of tags to get the maching tags for each line.

key_words = ['INDI','NAME','SEX','BIRT','DEAT','FAMC','FAMS','FAM','MARR','HUSB','WIFE','CHIL','DIV','DATE','HEAD','TRLR','NOTE']

#opening file

text_file = open('C:\Users\shree\Canopy\My-Family-18-May-2016-582.ged', 'r')

print "Printing each line of gedcom file followed by level no and tag line"

#Looping through each line 
for line in text_file:
    
    print "line is:-", line
    
    # getting level no
    
    level_number = int(line[:1])
    
    print "Level number is",level_number   
    
    #spliting the line into individual word
    line_words = line.split()
    
    # get the first element since that is the tag of line
    line_tag = line_words[1].strip() 

    # check if that is present in the keywords
    if line_tag in key_words:
        
        print "Tag is:-",line_tag,"\n"
        
    elif 'INDI' in line:
        
        print 'The tag name is :- INDI \n'
    
    else:
        
        print "invalid tag \n"




