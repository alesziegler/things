from customer import Customer
from database import Database


class Interface:
    """
    Instance  of this class
    1) takes user input from Menu,
    2) decides what to do based on it,
    3) handles all communication with users after they pick an option in Menu
    4) adds created customers to database?
    """

    def __init__(self):
        self.database = Database()
        self.print_options()
        self.chosen_action = self.make_user_pick()

        while self.chosen_action != "4":

            if self.chosen_action == "1":
                self.add_new_customer()
            elif self.chosen_action == "2":
                self.print_all_customers()
            elif self.chosen_action == "3":
                self.find_customer()
            else:
                self.handling_invalid_input()
            self.print_options()
            self.chosen_action = self.make_user_pick()
        self.exit()


    def print_options(self):

        print("""
        Vase moznosti:\n
        1 - Pridat noveho pojisteneho\n
        2 - Vypsat vsechny pojistene\n
        3 - Vyhledat pojisteneho\n
        4 - Konec
        """)

    def make_user_pick(self):
        chosen_action = input("Vyberte si akci ze seznamu vyse: ")
        return chosen_action


    def add_new_customer(self):
        """
        There are several pieces that need to be put together.
        Validation should be done through while loop(s) connected
        ...

        :return:
        """
        name_invalid = True
        contact_invalid = True
        age_invalid = True

        new_customer = Customer()

        while name_invalid:

            given_name = input("Zadejte krestni jmeno pojistence (bez mezer): ")
            surname = input("Zadejte prijmeni pojistence (bez mezer): ")
            full_name = (given_name, surname)

            try:
                new_customer.name = full_name
            except ValueError as error_message:
                #this is a custom message, defined in setter
                print(error_message)
            else:
                name_invalid = False

        while contact_invalid:
            contact = input("Zadejte telefon pojistence: ")
            try:
                new_customer.contact = contact
            except ValueError as error_message:
                # this is a custom message, defined in setter
                print(error_message)
            else:
                contact_invalid = False



        age = input("Zadejte vek pojistence: ")
        Customer.age = age
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
    Right now, this method is superfluous, but what if
    I decide to add some other functionality
    (e.g. sending some data somewhere before app closes)
    """
        return

    def handling_invalid_input(self):
        print("Tohle neni spravna volba. Vyberte si prosim lepe.")
