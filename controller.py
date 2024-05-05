class Controller:
    """
    This class
    1) takes user input from menu,
    2) decides what to do based on it,
    3) handles all communication with users after they pick an option in menu
    """
    def __init__(self, chosen_action):
        self.chosen_action = chosen_action
        """
        Here we need to relocate integer conversion from menu
        and validation mechanism in case user writes something
        non-convertible
        """
        try:
            self.chosen_action = int(self.chosen_action)
        except:
            self.handling_invalid_input()

        if self.chosen_action == 4:
            self.ending()
        else:
            if self.chosen_action == 1:
                self.add_new_customer()
            elif self.chosen_action == 2:
                self.print_all_customers()
            elif self.chosen_action == 3:
                self.find_customer()
            else:
                self.handling_invalid_input()
            from menu import Menu
            Menu()

    def add_new_customer(self):
        pass

    def print_all_customers(self):
        pass

    def find_customer(self):
        pass

    def ending(self):
        return

    def handling_invalid_input(self):
        """
        Ok, this always leads back to a new menu

        """
        print("Tohle neni validni volba. Vyberte si lepe.")
        return self
