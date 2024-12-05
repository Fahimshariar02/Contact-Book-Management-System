import add_contacts
import view_data
import search_contact
import remove_contact
import load_previous_contact

all_info = []

while True:
    print("Welcome to Contact Book Management System")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    
    menu = input("Choose an option: ")
    
    if menu == "0":
        print("Thanks for using Contact Book Management System")
        break
    elif menu == "1":
        # This section is for load the previous data and append/add new data
        all_info = load_previous_contact.previous_contacts() 
        all_info = add_contacts.addContacts(all_info)
    elif menu == "2":
        view_data.viewData()
    elif menu =="3":
        search_contact.searchContact()
    elif menu =="4":
        remove_contact.removeContact()
    else:
        print("Choose a valid number")