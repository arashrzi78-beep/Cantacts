contacts = {}

while True:
    print("<--- Contact Details --->")
    print("<--- press 1 to add a contact --->")
    print("<--- press 2 to show all contacts --->")
    print("<--- press 3 to search for a contact --->")
    print("<--- press 4 to delete a contact --->")
    print("<--- press 5 to Quit --->")

    choice = input("choose a number: ")

    if choice == "1":
        name = input("name: ").lower()
        phone = input("phone number: ")
        contacts[name] = phone
        print(" added successfully.")

    elif choice == "2":
        if contacts:
            print("\n contacts :")
            for name, phone in contacts.items():
                print(f"{name} --> {phone}")
        else:
            print(" its empty")

    elif choice == "3":
        search_name = input("name to search: ").lower()
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print(" not found.")

    elif choice == "4":
        del_name = input("nome to delete: ").lower()
        if del_name in contacts:
            del contacts[del_name]
            print(" deleted successfully.")
        else:
            print(" not found.")

    elif choice == "5":
        print(" Take care!")
        break

    else:
        print(" try again.")