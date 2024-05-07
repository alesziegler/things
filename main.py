
from menu import Menu

print()
print("***EVIDENCE POJISTENYCH***")
print()

"""
Maybe we could do inception in a following way:
1) controller (interface) object is initialized,
2) it imediately initializes Menu object
3) Optional intermediate step - menu object creation might be 
in a separate method?
4) ?? Menu object returns, in constructor, chosen action?
5) chosen action is then passed to decision tree
"""

Menu()

"""
ok, key unknown which we now face is how to properly
construct database
"""

print('This is The End')