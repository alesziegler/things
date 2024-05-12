from customer import Customer
from database import Database


class Interface:
    """
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

    def validate_input(self, boolean, property_of_object, prompt1, prompt2=None):
        """
         (Unfortunately this doesn't work;
         I am leaving it here in the hope that I'll be able to fix that later)
        """
        pass
        """
        This static method abstracts validation of user input, to avoid repeating code:
        :param boolean:
            while True, user is repeatedly asked for input.
            It becomes False when correct input is received from user.
        :param property_of_object:
        this is the property where we put validated input.
        :param prompt1:
        Variable input prompt.
        :param prompt2:
        optional second input prompt (here used for validating name(given_name,surname))
        """
        """
        while boolean:
            data_added_to_object = input(prompt1)
            if prompt2 is not None:
                additional_data = input(prompt2)
                data_added_to_object = (data_added_to_object, additional_data)
            try:
                property_of_object = data_added_to_object
            except ValueError as error_message:
                # this is a custom message, defined in property setter
                print(error_message)
            else:
                # when validation successful, boolean switches and process moves on:
                boolean = False
        """

    def add_new_customer(self):

        name_invalid = True
        contact_invalid = True
        age_invalid = True

        new_customer = Customer()

        """
        unfortunately this doesn't work
        (it asks for inputs,but it fails to pass input into setter,
        and continues with the next step):
        self.validate_input(
            name_invalid,
            new_customer.name,
            "Zadejte krestni jmeno pojistence (bez mezer): ",
            "Zadejte prijmeni pojistence (bez mezer): "
        )

        """
        while name_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            given_name = input("Zadejte krestni jmeno pojistence (bez mezer): ")
            surname = input("Zadejte prijmeni pojistence (bez mezer): ")
            full_name = (given_name, surname)

            try:
                new_customer.name = full_name
            except ValueError as error_message:
                # this is a custom message, defined in setter:
                print(error_message)
            else:
                name_invalid = False

        while age_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            age = input("Zadejte vek pojistence: ")
            try:
                new_customer.age = age
            except ValueError as error_message:
               # this is a custom message, defined in setter:
               print(error_message)
            else:
                age_invalid = False

        while contact_invalid:
            # this a stupidly repetitive way to do validation since clever method above doesn't work
            contact = input("Zadejte telefon pojistence: ")
            try:
                new_customer.contact = contact
            except ValueError as error_message:
                # this is a custom message, defined in setter:
                print(error_message)
            else:
                contact_invalid = False

        self.database.add_new_customer(new_customer.identifiers)

    def print_all_customers(self):
        # this should be done via str of database
        print(self.database)

    def find_customer(self):
        print("""
        Chcete vyhledat pojisteneho:\n
        1) podle jmena a prijmeni?\n
        2) podle veku?\n
        3) podle telefoniho cisla?\n
        4) rozmyslel jsem si to. Nic hledat nechci.
        """)
        query = self.make_user_pick()

        while query != "4":
            if query == "1":
                name_query = input("Zadejte prosim hledane jmeno a prijmeni, oddelene mezerou: ")
                self.database.find_customer_by_category("name",name_query)
            elif query == "2":
                age_query = input("Zadejte prosim hledany vek: ")
                self.database.find_customer_by_category("age",age_query)
            elif query == "3":
                contact_query = input("Zadejte prosim hledane telefonni cislo (9 cislic bez mezer: ")
                self.database.find_customer_by_category("contact",contact_query)
            else:
                self.handling_invalid_input()
                self.find_customer()
        print("Ok. Vitejte zpatky v hlavnim menu.")
        self.exit()



    def exit(self):
        """
    Right now, this method is superfluous, but what if
    I decide to add some other functionality
    (e.g. sending some data somewhere before app closes)
    """
        return

    def handling_invalid_input(self):
        print("Tohle neni spravna volba. Vyberte si prosim lepe.")
