#Main Codespace

class Employee:
    def __init__(self, name, record):
        self.name = name
        self.record = record


class Host(Employee):
    pass


class Cook(Employee):
    pass


class Waiter(Employee):
    pass

class Organization:
    def __init__(self, name, employees):
        #def create_organization
        #def add_employee -- ???
        pass


def home_menu():
    print("Home Menu")
    print("1. Choose/Add Organization")
    print("2. View Organizations")


home_menu()