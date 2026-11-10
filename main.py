#Main Codespace

class Employee:
    def __init__(self, name):
        self.name = name
        self.report_log = []


class Host(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.parties_seated = 0


class Cook(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.orders_prepared = 0


class Waiter(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.tables_served = 0

class Other(Employee):
    def __init__(self, name):
        super().__init__(name)

class Organization:
    pass


def home_menu():
    while True:
        print("Home Menu")
        print("1. Choose/Add Organization")
        print("2. View Organizations")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            organization_menu()
        elif choice == "2":
            pass
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def organization_menu():
    while True:
        print("Organization Menu")
        print("1. Choose Organization")
        print("2. Add Organization")
        print("3. Back")

        choice = input("Enter your choice: ")
        if choice == "3":
            return
        elif choice not in ("1", "2"):
            print("Invalid choice")


home_menu()