
from menu import Menu
class Controller:

    def __init__(self,chosen_action):
        self.chosen_action = chosen_action
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
                self.error_messaging()
            View("Pokracujte libovolnou klavesou...")

    def add_new_customer(self):
        pass

    def print_all_customers(self):
        pass

    def find_customer(self):
        pass

    def ending(self):
        print('This is The End')

    def error_messaging(self):
        self.chosen_action = int(
            input("REPENT:")
        )
        return self