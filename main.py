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
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


def home_menu():
    organizations = []
    while True:
        print("Home Menu")
        print("1. Choose/Add Organization")
        print("2. View Organizations")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            organization_menu(organizations)
        elif choice == "2":
            view_organizations(organizations)
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def view_organizations(organizations):
    if not organizations:
        print("Nothing here yet")
    else:
        print("Organizations:")
        for organization in organizations:
            print(organization.name)

    input("Type anything to go back: ")


def organization_menu(organizations):
    while True:
        print("Organization Menu")
        print("1. Choose Organization")
        print("2. Add Organization")
        print("3. Back")

        choice = input("Enter your choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            name = input("Organization name: ")
            organizations.append(Organization(name))
            print(f"Added {name}")
        elif choice == "3":
            return
        else:
            print("Invalid choice")


home_menu()