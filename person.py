class Person:
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

        self.__tel = None
        self.__age = None
        self.__identifiers = {
            "name":self.__name,
            "tel":self.__tel,
            "age":self.__age
        }

    def name_validation(self,name,locator): #maybe it should have as a paremeter jmeno or prijmeni
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
                    f"V {locator} nesmi byt mezery.")

        return name
    @property
    def name(self):
        print("property test")
        return self.__name

    @name.setter
    def name(self,n):
        """
        ideally there should be check
        whether name an surname has proper capitalization.
        Maybe it could be achieved via n being a tuple?
        :param n:
        :return:
        """
        print("setting name")
        if len(n) != 2:
            raise ValueError("Je nutno zadat jmeno a prijmeni (dve slova)")
        given_name = n[0]
        self.name_validation(given_name,"krestnim jmenu")
        surname = n[1]
        self.name_validation(surname,"prijmeni")

        #self.__name = check


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,a):
        #validation here (possibly fancy time stuff)
        self.__age = a

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self,t):
        ## if tel is not valid, "raise ValueError('tel needs to have 6 digits')"
        self.__tel = t

    def __str__(self):
        pass

