class Customer:
    """
    Ok, there will be protected attributes, changed via setter.
    In essence, it will be a dictionary.
    There will be two possible ways

    """
    def __init__(self):
        """
        here we need to construct validation mechanism.
        Maybe it should be via setter from the beginning? Yess
        Maybe we should merge name and surname into one property
        Also in add new customer in interface, we should call setter method,
        not class as a whole?
        """
        self.__name = None
        self.__contact = None
        self.__age = None
        self.__identifiers = {
            "name":self.__name,
            "tel":self.__contact,
            "age":self.__age
        }




    @property
    def name(self):
        print("property test")
        return self.__name

    @name.setter
    def name(self,n):
        """

        :param n:
        :return:
        """
        print("setting name")
        if len(n) != 2:
            """
            Name has to be two objects in an iterable (given name and surname). 
            This validation step is superflous in this app because of the way input is entered. 
            But if customer class would be repurposed for something else, it would be essential.
            """
            raise ValueError("Je nutno zadat jmeno a prijmeni (dve slova)")

        given_name = n[0]
        surname = n[1]
        """
        If following validation doesn't work, it raises ValueError. 
        (with various error messages depending on what exactly is wrong with input). 
        How that error is handled depends on external interface.
        """
        self.name_validation(given_name,"krestnim jmenu")
        self.name_validation(surname,"prijmeni")
        # if no error is raised, name attribute is set:
        self.__name = given_name + " " + surname

    def name_validation(self,name,locator):
        """

        :param name:
        :param locator:
        :return:
        """
        print("name validation")
        czech_alphabet = "abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž"
        for letter in name:
            if letter.lower() not in czech_alphabet:
                raise ValueError(
                    f"Vsechny znaky v {locator} musi byt soucasti ceske abecedy. "
                    f"V {locator} nesmi byt mezery. Zadejte prosim jmeno i prijmeni znovu")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a):
        #validation will here (possibly fancy datetime stuff, or just integer > 18, if I'll get lazy)
        self.__age = a

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self,t):
        #validation will be here.
        # contact should have length 6 and should be convertible to an integer.
        self.__contact = t

    def __str__(self):
        return self.name, self.contact, self.age

