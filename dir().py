
# ************  dir()

# ************  dir() function is a built-in function used to list 
# ************  the attributes (methods, properties, and other members) 
# ************  of an object.


# Creation of a simple class with __dir()__
# method to demonstrate it's working
class Supermarket:
 
    # Function __dir()___ which list all 
    # the base attributes to be used.
    def __dir__(self):
        return['customer_name', 'product',
               'quantity', 'price', 'date']
 
 
# user-defined object of class supermarket
my_cart = Supermarket()
 
# listing out the dir() method
print('*******',dir(my_cart))

# output
# ['customer_name', 'date', 'price', 'product', 'quantity']


# Python3 code to demonstrate dir()
# when no parameters are passed
# Note that we have not imported any modules
print(dir())

# output
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
 
# Now let's import two modules
import random
import math
 
print(dir())



# When a list object is passed as 
# parameters for the dir() function
 
# A list, which contains
# a few random values
vats = ["data scientist", "cag", "Computer Science",
                    "Data Structures", "Algorithms" ]
 
# dir() will also list out common
# attributes of the dictionary
d = {}   # empty dictionary
 
# dir() will return all the available 
# list methods in current local scope
print(dir(vats))

# output
#  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

print(dir(d))

# output
#  ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

