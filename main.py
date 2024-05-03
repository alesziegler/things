
from controller import Controller

print()
print("***EVIDENCE POJISTENYCH***")
print()

print("1 - Pridat noveho pojisteneho")
print("2 - Vypsat vsechny pojistene")
print("3 - Vyhledat pojisteneho")
print("4 - Konec")
print()
chosen_action = int(
    input("Vyberte si akci ze seznamu vyse:")
)
"""
after the user chooses what they want, a controller object is initialized and
takes over the action:
"""
Controller(chosen_action)