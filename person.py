class Person:
    """
    Ok, there will be protected attributes, changed via setter.
    In essence, it will be a dictionary.

    """
    def __init__(self, name, tel, age):
        """
        here we need to construct validation mechanism.
        Maybe it should be via setter from the beginning? Yess
        Maybe we should merge name and surname into one property
        Also in add new customer in interface, we should call setter method,
        not class as a whole?
        """
        self.__name = name

        self.__tel = tel
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,n):
        """
        ideally there should be check
        whether name an surname has proper capitalization
        :param n:
        :return:
        """
        self.__name = n

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
        #validation here
        self.__tel = t

    def __str__(self):
        pass

