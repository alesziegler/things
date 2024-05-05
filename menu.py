from controller import Controller


class Menu:
    """
    This class handles menu

    """

    def __init__(self):
        """
        Every time menu is initialized,
        four things happen:
        1) options are shown to a user,
        2) user is asked to pick one,
        3) picked option is then stored to a public variable (named chosen_action),
        4) controller object is initialized with chosen action as a parameter
        """
        self.print_options()
        self.chosen_action = self.make_user_pick()
        Controller(self.chosen_action)

    def print_options(self):
        menu = """
        Vase moznosti:\n
        1 - Pridat noveho pojisteneho\n
        2 - Vypsat vsechny pojistene\n
        3 - Vyhledat pojisteneho\n
        4 - Konec
        """
        return print(menu)

    def make_user_pick(self):
        chosen_action = int(
            input("Vyberte si akci ze seznamu vyse:")
        )
        return chosen_action