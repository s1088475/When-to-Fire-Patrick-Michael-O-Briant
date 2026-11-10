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

    if input("Enter your choice: ") == "1":
        pass
    elif input("Enter your choice: ") == "2":
        pass
    else:
        print("Invalid choice")


home_menu()