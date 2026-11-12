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
    selected_organization = None
    while True:
        print("Organization Menu")
        if selected_organization is not None:
            print(f"Selected: {selected_organization.name}")
        print("1. Choose Organization")
        print("2. Add Organization")
        print("3. Back")

        choice = input("Enter your choice: ")
        if choice == "1":
            selected = choose_organization(organizations)
            if selected is not None:
                selected_organization = selected
                employee_menu(selected)
        elif choice == "2":
            name = input("Organization name: ")
            organizations.append(Organization(name))
            print(f"Added {name}")
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def choose_organization(organizations):
    if not organizations:
        print("Nothing here yet")
        input("Type anything to go back: ")
        return None

    print("Choose an Organization:")
    for index, organization in enumerate(organizations, start=1):
        print(f"{index}. {organization.name}")
    print("0. Back")

    choice = input("Enter your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(organizations):
        selected = organizations[int(choice) - 1]
        print(f"Selected {selected.name}")
        return selected

    if choice != "0":
        print("Invalid choice")
    return None


def employee_menu(organization):
    while True:
        print(f"Employee Menu - {organization.name}")
        print("1. View Existing Employees")
        print("2. Create New Employee")
        print("3. Back")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_employees(organization)
        elif choice == "2":
            add_employee_to_organization(organization)
        elif choice == "3":
            return
        else:
            print("Invalid choice")


def view_employees(organization):
    if not organization.employees:
        print("Nothing here yet")
    else:
        print(f"Employees at {organization.name}:")
        for employee in organization.employees:
            role = employee.__class__.__name__.lower()
            print(f"{employee.name} - {role}")

    input("Type anything to go back: ")


def add_employee_to_organization(organization):
    employee_types = {
        "1": ("cook", Cook),
        "2": ("waiter", Waiter),
        "3": ("host", Host),
        "4": ("other", Other),
    }

    while True:
        print("Choose a job type:")
        print("1. Cook")
        print("2. Waiter")
        print("3. Host")
        print("4. Other")
        choice = input("Enter your choice: ").strip()
        if choice in employee_types:
            job, employee_type = employee_types[choice]
            break
        print("Invalid choice")

    name = input("Employee name: ").strip()
    organization.add_employee(employee_type(name))
    print(f"Added {name} as {job} to {organization.name}")


home_menu()