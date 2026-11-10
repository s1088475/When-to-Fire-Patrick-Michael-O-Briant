#Main Codespace

class Employee:
    pass


class Host(Employee):
    pass


class Cook(Employee):
    pass


class Waiter(Employee):
    pass

class Organization:
    pass


def home_menu():
    print("Home Menu")
    print("1. Choose/Add Organization")
    print("2. View Organizations")
    print("3. Quit")

    choice = input("Enter your choice: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("Invalid choice")


home_menu()