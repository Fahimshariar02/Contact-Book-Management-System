def searchContact():
    while True:
        phone = input("Enter the phone number which you want to search: ")
        if not phone.isdigit():
            print("Error: The user phone number must contain only digits. Please try again.")
            continue
        break


    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')
    
    isFound = False
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            break
        elif info[2] == phone:
            # All information is displayed based on the searched phone number
            print("Name:",info[0],"\t\tEmail:",info[1],"\t\tPhone Number:",info[2],"\t\tAddress:",info[3])
            isFound = True
            break
    
    if isFound == False:
        print("Sorry! The information that you want to search doesn't exist")
