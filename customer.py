class Customer:
    
    def __init__(self):
        
        self.__name = None
        self.__contact = None
        self.__age = None
        self.__identifiers = {
            "name": self.__name,
            "tel": self.__contact,
            "age": self.__age
        }

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        """

        :param n:
        :return:
        """
        if len(n) != 2:
            """
            Name has to be two objects in an iterable (given name and surname). 
            This validation step is superflous in this app because of the way input is entered, 
            but if Customer class would be repurposed for something else, it would be essential.
            """
            raise ValueError("Je nutno zadat jmeno a prijmeni (dve slova)")

        given_name = n[0]
        surname = n[1]

        try:
            self.name_validation(given_name, "krestnim jmenu")
            self.name_validation(surname, "prijmeni")
        except ValueError as error_message:
            raise ValueError(error_message)
        else:
            self.__name = given_name + " " + surname

    def name_validation(self, name, locator):

        czech_alphabet = "abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž"
        for letter in name:
            if letter.lower() not in czech_alphabet:
                raise ValueError(
                    f"Vsechny znaky v {locator} musi byt soucasti ceske abecedy. "
                    f"V {locator} nesmi byt mezery. Zadejte prosim krestni jmeno i prijmeni znovu."
                )

        if not name[0].isupper():
            raise ValueError(
                f"Prvni pismeno v {locator} musi byt velke. "
                f"Zadejte prosim krestni jmeno i prijmeni znovu."
            )
        if not name[1::].islower():
            """
            this is unfortunately triggered even when name has just one capital letter.
            I'll try to fix that.
            """
            raise ValueError(
                f"Velke pismeno muze byt v {locator} jen na zacatku. "
                f"Zadejte prosim krestni jmeno i prijmeni znovu."
            )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, a):
        #validation will here (possibly fancy datetime stuff, or just integer > 18, if I'll get lazy)
        self.__age = a

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, t):
        try:
            int(t)
        except ValueError:
            raise ValueError("telefoni cislo musi obsahovat pouze cislice bez mezer")
        else:
            self.__contact = t

        #validation will be here.
        # contact should have length 6 and should be convertible to an integer.

    @property
    def identifiers(self):
        return self.__identifiers


    def __str__(self):
        return self.name  # self.contact, self.age
