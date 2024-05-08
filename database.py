
class Database:
    """
    This class will have methods which
    will be called directly from controller.
    Probably it will essentially be a list of Persons,
    i.e. essentially list of dictionaries.
    It should def have add method, print all method, and find method
    add method should have an equal thing used for validation
    (so it would be impossible to have two identical customers)
    Maybe we should not store here person objects, but
    dictionaries roughly equivalent to them?

    """

    def __init__(self):
        self.__core = []

    def add_new_customer(self, new_customer):
        self.__core.append(new_customer)

    def __str__(self):
        """
        This will be used for fetching the whole database
        :return:
        """
        pass
