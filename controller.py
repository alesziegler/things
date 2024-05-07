from person import Person
from database import Database

class Controller:
    """
    Instance  of this class
    1) takes user input from Menu,
    2) decides what to do based on it,
    3) handles all communication with users after they pick an option in Menu
    4) adds created customers to database?
    """
    def __init__(self, chosen_action):
        """

        :param chosen_action: provisional setup
        """
        self.database = Database()
        self.chosen_action = chosen_action

        if self.chosen_action == "4":
            self.exit()
        else:
            if self.chosen_action == "1":
                self.add_new_customer()
            elif self.chosen_action == "2":
                self.print_all_customers()
            elif self.chosen_action == "3":
                self.find_customer()
            else:
                self.handling_invalid_input()

            from menu import Menu
            """
            internal import is here because when Menu is imported before init,
            interpreter screams at me that it is not allowed.
            Cycle with indeterminate number of repeats could also achieved
            in Menu class or in main via while (chosen_action != 4) print menu again and ask for input,
            but I think, maybe wrongly, that this is better.
            """
            Menu()

    def add_new_customer(self):
        given_name = input("Zadejte jmeno pojistence: ")
        surname = input("Zadejte prijmeni pojistence: ")
        n = given_name + " " + surname
        """
        So here should probably be a validation that 
        name and surname uses proper capitalization,
        since setter apparently cannot have two parameters.
        Maybe use lambda function for that?
        """
        Person.name = n
        tel = input("Zadejte telefon pojistence: ")
        Person.tel = tel
        age = input("Zadejte vek pojistence: ")
        Person.age = age
        """
        Ok, probably just here we need to add Person to a database?
        Maybe using __str__method in Person?? Probably not, that
        will be for printing and searching of a database??
        Or maybe we should add it in constructor of Person??
        OR, what about like this:
        new_costumer = Person()
        new_customer.name = n
        and so on. Then:
        Database.add(new_customer)
        Problem is, we need to connect database to interface
        Probably we should do that in interface constructor?
        """

    def print_all_customers(self):
        pass

    def find_customer(self):
        pass

    def exit(self):
        """
        Right know, this could be written directly
    into constructor, saving space, but what if
    I decide to add some other functionality
    (e.g. sending some data somewhere before app closes)
    """
        return

    def handling_invalid_input(self):
        print("Tohle neni validni volba. Vyberte si lepe.")

