from person import Person
from database import Database

class Controller:
    """
    This class
    1) takes user input from menu,
    2) decides what to do based on it,
    3) handles all communication with users after they pick an option in menu
    """
    def __init__(self, chosen_action):
        self.chosen_action = chosen_action

        if self.chosen_action == "4":
            self.ending()
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
        name = input("Zadejte jmeno pojistence: ")
        surname = input("Zadejte prijmeni pojistence: ")
        tel = input("Zadejte telefon pojistence: ")
        age = input("Zadejte vek pojistence: ")
        Person(name,surname,tel,age)

    def print_all_customers(self):
        pass

    def find_customer(self):
        pass

    def ending(self):
        """
        Right know, this could be written directly
    into constructor, saving space, but what if
    I decide to add some other functionality
    (e.g. sending some data somewhere before app closes)
    """
        return

    def handling_invalid_input(self):
        print("Tohle neni validni volba. Vyberte si lepe.")

