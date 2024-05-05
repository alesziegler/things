
class View:
    """
    Only purpose of an object of this class is to ensure that
    new controller object is initialized every time
    previous interaction ends, until users ends the program.
    (I don't know whether this is a 'proper' way to do it):
    """
    def __init__(self,message_to_user):
        print(message_to_user)


