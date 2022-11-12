contacts = []

activity = input("Welcome to your contact list, please press 'enter'/'return' to start, or 'exit' to exit the program): ")


def insert(nam, num):
    """Uses list concatenation to insert a new name and number to the end of the contacts list"""
    temp = [nam + ": " + num]
    global contacts
    contacts += temp
    return contacts


def search(lst, nam, usage):
    """Searches for the contact information of the name provided by the user. Uses the Sequential Search Algorithm """
    i = 0

    while i < len(lst):
        if lst[i].startswith(nam):
            if usage == "d":
                return i
            else:
                return lst[i]
        else:
            i += 1
    return nam + " not in contacts"


def delete(lst, nam):
    """Deletes the name and number of a contact from contacts. Uses the earch function to find the contact
    and list slicing to remove the contact from the list"""
    global contacts
    entry_index = search(lst, nam, "d")
    if type(entry_index) == int:
        lst = lst[:entry_index] + lst[entry_index + 1:]
        return nam + " deleted"
    else:
        return entry_index


def sort(lst, asc_des):
    """Sorts contacts by names in an ascending order, unless descending order is selected by the user.
    Uses the Insertion Sort Algorithm"""
    i = 1

    if len(lst) == 0:
        return "List is empty, no entries to sort"
    else:
        #Sort list in ascending order
        if asc_des:
            while i < len(lst):
                """Outer loop, ensures that the entry we're checking is saved and setting the comparison 
                to the prior entry for as long as there are entries to check"""
                temp = lst[i]
                j = i - 1

                while j >= 0 and temp < lst[j]:
                    """Inner loop, ensures we're not trying to go byond index 0 and checkes if our entry is smaller
                    than the previous entry"""
                    lst[i] = lst[j]
                    i -= 1
                    j -= 1
                lst[i] = temp
                i += 1
            return lst

        else:
            #Sort list in descending order
            while i < len(lst):
                temp = lst[i]
                j = i - 1

                while j >= 0 and temp > lst[j]:
                    lst[i] = lst[j]
                    i -= 1
                    j -= 1
                lst[i] = temp
                i += 1
        return lst


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