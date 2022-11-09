contacts = []
action = input("Please enter the action you wish to take (add, delete, search, sort): ")
name = input("Please enter the contact's name: ")
number = input("Please enter the contact's phone number: ")
i = 0

def action(activity):
    """Allows the user to chose the activity they wish to perform"""
    if activity.lower() == "add":
        insert(name, number)
    elif activity.lower() == "delete":
        delete(name)
    elif activity.lower() == "search":
        search(name)
    elif activity.lower() == "sort":
        order = input("Please enter asc for ascending order or des for descending order: ")
        if order.lower() == "des":
            sort(contacts, False)
        else:
            sort(contacts, True)
    else:
        action()


def insert(name, number):
    """Inserts a new name and number to contacts"""
    temp = [name, number]
    global contacts
    contacts += temp
    return contacts


def search(name):
    """Searches for the contact information of the name provided by the user"""
    global i
7	    while i < len(contacts):
8	        if name == contacts[i]:
9	            return i and i+1
10	        else:
11	            i += 2
12	    return "contact not in list"


def delete(name):
    """Deletes the name and number from contacts"""
    search(name)
    global contacts
    contacts = contacts[:name] + contacts[name+2:]


def sort(contacts, True):
    """Sorts contacts by names in an ascending order, unless descending order is selected by the user"""

