# ******--Meaning of _ & __ in python

class student():
  def __init__(self):
    self.a=5
    self._b=10
    self.__c=20

obj=student()
print(obj.a)
print(obj._b)
# print(obj.__c)  # output will throw error, reason is the <__c> value cannot be
                  # accessed directly, instead <obj.student__c>

d=dir(obj)
print("<dir()> result is", d)

print(obj._student__c)  # __c can be accessed by this way

# Output
# 5
# 10
# <dir()> result is " ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
#  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
#  '__weakref__', '_b', '_student__c', 'a']
# 20
