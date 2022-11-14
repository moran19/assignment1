contacts = []

activity = input("Welcome to your contact list, please press 'enter'/'return' to start, or 'exit' to exit the program): ")


def insert(nam, num):
    """Uses list concatenation to insert a new name and number to the end of the contacts list"""
    temp = [nam + ": " + num]
    global contacts
    contacts += temp
    return contacts


def search(lst, nam):
    """Searches for the contact information of the name provided by the user. 
    Uses the Sequential Search Algorithm """
    i = 0

    while i < len(lst):
        if entry starts with name:
            if used in the delete function:
                return index number
            else:
                return contact details
        else:
            i += 1
    return  "name not in contacts"


def delete(lst, nam):
    """Deletes the name and number of a contact from contacts. 
    Uses the search function to find the contact
    and list slicing to remove the contact from the list"""
    global contacts
    entry_index = index of search result
    if entry_index is int:
        lst = lst[:entry_index] + lst[entry_index + 1:]
        return "name deleted"
    else:
        return "name not in contacts"


def sort(lst, asc_des):
    """Sorts contacts by names in an ascending order, unless descending order is selected by the user.
    Uses the Insertion Sort Algorithm"""
    i = 1

    if in ascending order:
        while i < len(lst):
            temp = lst[i]

            while there are entries prior to temp and temp is smaller than previous entry:
                entry = previous entry
                continue checking previous entries
            update temp in its right location
            i += 1
        return lst
    else:
        reverse of above



def action():
    """Allows the user to chose which of the following activity they wish to perform: add, delete, search, sort
    or exit for exiting the program"""
    activity = input("Please enter the action you wish to take (add, delete, search, sort or exit the program): ")

    if activity.lower() == "add":
        name = input("Please enter the contact's name: ")
        number = input("Please enter the contact's phone number: ")
        return insert(name, number)
    elif activity.lower() == "delete":
        name = input("Please enter the contact's name: ")
        return delete(contacts, name)
    elif activity.lower() == "search":
        name = input("Please enter the contact's name: ")
        return search(contacts, name, "s")
    elif activity.lower() == "sort":
        lst_order = input("Please enter 'asc' for ascending order or 'des' for descending order: ")
        if lst_order.lower() == "des":
            return sort(contacts, False)
        else:
            return sort(contacts, True)
    elif activity.lower() == "exit":
        quit()
    else:
        action()


while activity != "exit":
    print(action())