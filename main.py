#Main Codespace

class Employee:
    def __init__(self, name):
        self.name = name
        self.report_log = []


class Host(Employee):
    pass


class Cook(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.orders_prepared = 0


class Waiter(Employee):
    pass

class Other(Employee):
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