#Practice programming with GEDCOM data Assignment:
#programer - Siddhesh Palav
#Prof. Rowland
# asking user to input file name/ address.

#creating list of tags to get the maching tags for each line.

key_words = ['INDI','NAME','GIVN','SURN','_MARNM','SEX','BIRT','DATE','DEAT','HUSB','WIFE']

#creating list to save information about individuals
data = []

#creating list to store unique ID and associated names

ID_1 = []
Name_1 = []

#Creating dictionary to access both uniqueID and names
ID_name_dict_1 = {}  

#Reading file
gedcom_file = open('C:\Users\shree\Canopy\My-Family-18-May-2016-582.ged', 'r')

print "Printing each line of gedcom file followed by level no and tag line"

for line in gedcom_file:
    
    line_words = line.split()
    
    line_tag = line_words[1].strip()
    
    #Accessing level number of each line
    level_number = int(line[:1]) 
    
    #Adding all the lines in list realated to tags mentioned in key_words
    
    if line_tag in key_words:
        data.append(line)
   
   #Adding INDI tag in list 
    if 'INDI' in line:
        data.append(line)
    
    #Adding FAM lines in list
    if 'FAM' in line and level_number == 0:
        data.append(line)
    
print "All the saved information about individuals and families data is as follows"

print "\n"

for line in data:
    print line  
    
    #Printing unique ID
    if 'INDI' in line:
        extract = line[1:6]
        print "Unique id for the individual tag is:-",extract
        #adding data to list
        ID_1.append(extract)
    
    #Printing unique Name
    if 'NAME' in line:
        extract_1 = line[6:]
        print "the name associated with uniqueID is:-", extract_1
        #adding data to list
        Name_1.append(extract_1)

    if 'HUSB' in line:
        extract_3 = line[6:11]
        
        
    if 'FAM' in line:
        extract_5 = line[1:6]
        print "Unique ID for the FAM is :-",extract_5
    
    if 'WIFE' in line:
        extract_4 = line[6:11]
        
        
    #using dictionary for printing HUSB and WIFE name according to their unique tags
        for i in range(len(ID_1)):
            ID_name_dict_1 [ID_1[i]] = Name_1[i]  
        for keys_1,values_1 in (ID_name_dict_1.items()):
            if keys_1 == extract_4:
                print "Unique ID for HUSB is:-",extract_3
                print "The name of the HUSB is:-",values_1
            if keys_1 == extract_3:
                print "Unique ID for WIFE is:-",extract_4
                print "The Name of the Wife is:-",values_1
 
    
    

    
    
    