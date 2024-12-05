import save_data

def removeContact():
    while True:
        phone = input("Enter the phone number which you want to remove: ")
        if not phone.isdigit():
            print("Error: The user phone number must contain only digits. Please try again.")
            continue
        break


    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')

    isFound = False
    new_info = []
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            break
        else:
            if info[2] != phone:
                new_info.append(info)
            else:
                isFound = True
    
    if isFound == False:
        print("Sorry! The information that you want to remove doesn't exist")
    else:
        save_data.saveData(new_info)
        print(f"All information for phone number: {phone}, are removed successfully")
