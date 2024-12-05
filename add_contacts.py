from save_data import saveData
import load_previous_contact

single_info = []

def addContacts(all_info):
    # These two lines for loading previous data from file
    phone_list = load_previous_contact.load_phone_list()
    phone_set = load_previous_contact.load_phone_set()

    while True:
        name = input("Enter User Name: ")
        # This condition validates the name format and displays an error if it's incorrect. 
        if not name.isalpha():
            print("Error: The user name must contain only alphabetic characters. Please try again.")
            continue

        break
            
    while True:
        email = input("Enter User Email: ")
        # This condition validates the email format and displays an error if it's incorrect. 
        if not email[0].isalpha() or email.isalpha() or email.isdigit():
            print("Error: The user email must contain alphabetic characters, digits and special characters also. Please try again.")
            continue
        break

    while True:
        phone = input("Enter User Phone Number: ")

        # Prevention of duplicate phone numbers is implemented here by showing the error message
        phone_list.append(phone)
        phone_set.add(phone)
        # This condition validates the phone number format and displays an error if it's incorrect. 
        if len(phone_list) == len(phone_set):
            if not phone.isdigit():
                value = phone_list.pop()
                phone_set.remove(value)
                print("Error: The user phone number must contain only digits. Please try again.")
                continue
        else:
            phone_list.pop()
            print("Error: You can't store same phone number for different users. Please enter differnt phone Number.")
            continue

        break
    #Address could be acharacter as well as digits. So we don't need to add any condition
    address = input("Enter User Address: ") 

    single_info.append(name)
    single_info.append(email)
    single_info.append(phone)
    single_info.append(address)

    # Here we need to add the single user information into a lsit
    all_info.append(single_info[:])
    single_info.clear()

    saveData(all_info)
    return all_info
