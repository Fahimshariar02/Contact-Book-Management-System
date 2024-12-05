def viewData():
    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')
    
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            print("Sorry! No information is added yet")
        else:
            print("Name:",info[0],"\t\tEmail:",info[1],"\t\tPhone Number:",info[2],"\t\tAddress:",info[3])
