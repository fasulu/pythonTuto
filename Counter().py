
# ************  Counter()

'''   Counter() is a sub-class that is used to count hashable objects. 
        It implicitly creates a hash table of an iterable when invoked.
      elements() is one of the functions of Counter class, when invoked 
        on the Counter object will return an itertool of all the known 
        elements in the Counter object.
        
        Applications: 
        Counter object along with its functions are used collectively 
        for processing huge amounts of data. We can see that Counter() 
        creates a hash-map for the data container invoked with it which 
        is very useful than by manual processing of elements. 
        It is one of a very high processing and functioning tools and 
        can even function with a wide range of data too.
'''
from collections import Counter

data = 'Welcome to Children In Needs'
result = Counter(data)
print(result)   # print how many times each charcter appear in given data string

# output of result
'''
Counter({'e': 5, ' ': 4, 'l': 2, 'o': 2, 'd': 2, 'n': 2, 'W': 1, 'c': 1, 'm': 1, 't': 1, 'C': 1, 'h': 1, 'i': 1, 'r': 1, 'I': 1, 'N': 1, 's': 1})
'''

print(result['e'])  # output is 5

for x in 'to':
    print(x,result[x])

# output
'''
t 1
o 2
'''

#Creating a Counter class object using list as an iterable data container
a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
 
x = Counter(a)
 
#directly printing whole x
print('@1:- ', x)
 
#We can also use .keys() and .values() methods to access Counter class object
for i in x.keys():
      print('@2:- ', i, ":", x[i])
     
#We can also make a list of keys and values of x
x_keys = list(x.keys())
x_values = list(x.values())
 
print('@3:- ', x_keys)
print('@4:- ', x_values)

# output
'''
@1:-  Counter({12: 2, 3: 2, 4: 1, 5: 1, 11: 1, 6: 1, 7: 1})
@2:-  12 : 2
@2:-  3 : 2
@2:-  4 : 1
@2:-  5 : 1
@2:-  11 : 1
@2:-  6 : 1
@2:-  7 : 1
@3:-  [12, 3, 4, 5, 11, 6, 7]
@4:-  [2, 2, 1, 1, 1, 1, 1]

'''

# import Counter from collections
from collections import Counter
 
# creating a raw data-set using keyword arguments
x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)
 
# printing out the elements
for i in x.elements():
    print( "% s : % s" % (i, x[i]), end ="\n")      # negative value is omitted

# output
'''
We can notice from the output that items with values less than 1 are omitted by elements().
a : 2
a : 2
x : 3
x : 3
x : 3
b : 3
b : 3
b : 3
z : 1
y : 5
y : 5
y : 5
y : 5
y : 5

'''