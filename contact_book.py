contacts = []

#Welcome message
activity = input("Welcome to your contact list, please press 'enter'/'return' to start, or 'exit' to exit the program: ")


def insert(lst, nam, num):
    """Uses list concatenation to insert a new name and number to the end of the contacts list"""

    confirm = input("Are you sure you wish to add {}: {}? Enter 'yes'/'y' or 'no': ".format(nam, num))
    temp = [nam + ": " + num]

    if confirm.lower() == "yes" or confirm.lower() == "y":
        global contacts
        lst += temp
        return lst
    else:
        return nam + " was not added"


def search(lst, nam, usage):
    """Searches for the contact information of the name provided by the user.
    Uses the Sequential Search Algorithm """
    i = 0
    match = []

    # When used for search
    if usage != "d":
        confirm = input("Are you sure you wish to find {}? Enter 'yes'/'y' or 'no': ".format(nam))
        if confirm.lower() == "yes" or confirm.lower() == "y":
            for name in lst:
                if nam.lower() in name.lower():
                    match.append(name)
        else:
            return "No action was taken"

        if match == []:
            return nam + " not in contacts"
        else:
            return match

    # When used in the delete function, returns index number.
    #Makes sure the user is aware of the details to be deleted
    if usage == "d":
        while i < len(lst):
            if nam.lower() in lst[i].lower():
                confirm = input(
                    "Are you sure you wish to delete {}? This action cannot be undone. Enter 'yes'/'y' or 'no': ".format(lst[i]))
                if confirm.lower() == "yes" or confirm.lower() == "y":
                    return i
                else:
                    return "No action was taken"
            else:
                i += 1
        return nam + " not in contacts"



def delete(lst, nam):
    """Deletes the name and number of a contact from contacts.
    Uses the search function to find the contact
    and list slicing to remove the contact from the list"""
    global contacts
    entry_index = search(lst, nam, "d")
    if type(entry_index) == int:
        contacts = lst[:entry_index] + lst[entry_index + 1:]
        return nam + " deleted"
    else:
        return entry_index


def sort(lst, asc_des):
    """Sorts contacts by names in an ascending order, unless descending order is selected 
    by the user. Uses the Insertion Sort Algorithm"""

    i = 1

    if len(lst) == 0:
        return "List is empty, no entries to sort"
    else:
        #Sort list in ascending order
        if asc_des:
            confirm = input(
                "Are you sure you wish to sort the list in ascending order? Enter 'yes'/'y' or 'no': ")

            if confirm.lower() == "yes" or confirm.lower() == "y":
                while i < len(lst):
                    """Outer loop - ensures that the entry we're checking is saved and setting the comparison 
                    to the prior entry for as long as there are entries to check"""
                    temp = lst[i]
                    j = i - 1

                    while j >= 0 and temp < lst[j]:
                        """Inner loop - looks for a smaller entry to the left for as long as 
                        there are smaller entries to check"""
                        lst[i] = lst[j]
                        i -= 1
                        j -= 1
                    lst[i] = temp
                    i += 1
                return lst
            else:
                return "The list was not sorted"

        else:
            # Sort list in descending order
            confirm = input(
                "Are you sure you wish to sort the list in descending order? Enter 'yes'/'y' or 'no': ")

            if confirm.lower() == "yes" or confirm.lower() == "y":
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
            else:
                return "The list was not sorted"


def action():
    """Allows the user to chose which of the following activity they wish to perform: add, 
    delete, search, sort, print or exit"""

    activity = input("Please enter the action you wish to take (add, delete, search, sort or exit the program): ")

    if activity.lower() == "add":
        name = input("Please enter the contact's name: ")
        number = input("Please enter the contact's phone number: ")
        return insert(contacts, name, number)
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
    elif activity.lower() == "print":
        return contacts
    elif activity.lower() == "exit":
        quit()
    else:
        return "No action selected"

#Executes the program
while activity != "exit":
    print(action())


"""
#Testing

#Testing for adding 6 records
print(insert(contacts, "a", "1"))
print(insert(contacts, "b", "2"))
print(insert(contacts, "c", "3"))
print(insert(contacts, "d", "4"))
print(insert(contacts, "e", "5"))
print(insert(contacts, "f", "6"))

#Testing for searching records (1 that is in contacts and 1 that is not)
print(search(contacts, "d", "s"))
print(search(contacts, "g", "s"))

#Testing for deleting records (1 that is in contacts and 1 that is not)
print(delete(contacts, "d"))
print(delete(contacts, "g"))

#Testing for sorting records (once in ascending order and once in descending)
print(sort(contacts, True))
print(sort(contacts, False))
"""
