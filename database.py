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
        self.__core_database = []

    def add_new_customer(self, new_customer):
        for customer in self.__core_database:
            if customer == new_customer:
                raise ValueError("Tento pojistenec uz je v evidenci.")
            else:
                self.__core_database.append(new_customer)
        #print(new_customer.values())

    def find_customer_by_category(self,category, query):
        result = ""
        for customer in self.__core_database:
            if customer[category] == query:
                result += str(customer)
        return result

    def __str__(self):
        """
        This is used for fetching the whole database
        """
        printable_table = ""

        for customer in self.__core_database:
            printable_customer = (
                f"{customer['jmeno']},{customer['vek']},{customer['kontakt']}\n")
            printable_table += printable_customer
            """
             so, we need to do what?
             ideally, a matrix, somehow.
             First line would be: jmeno, vek, telefon
             """
        return printable_table
