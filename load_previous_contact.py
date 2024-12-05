def previous_contacts():
    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')
    allContacts = []
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            pass
        else:
            allContacts.append(info)

    return allContacts
            
def load_phone_list():
    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')
    phoneList = []
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            pass
        else:
            phoneList.append(info[2])

    return phoneList

def load_phone_set():
    with open("newFile.csv","r") as myfile:
        content  = myfile.read()

    Updated_content = content.strip().split('\n\n')
    phoneSet = set()
    for row in Updated_content:
        info = row.split(',')
        if info == ['']:
            pass
        else:
            phoneSet.add(info[2])

    return phoneSet