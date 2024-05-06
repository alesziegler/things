class Person:
    """
    Ok, there will be protected attributes, changed via setter.
    In essence, it will be a dictionary.

    """
    def __init__(self,name, surname, tel, age):
        self.__name = name
        self.__surname = surname
        self.__tel = tel
        self.__age = age
        # here we need to construct validation mechanism

    def checking_whether_initials_are_ok(self):
        pass