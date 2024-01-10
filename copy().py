
# ************  copy() module  

'''     Difference between copy vs shallow copy vs deep copy

'''

a=[[1,2,3],[4,5,6],[7,8,9]]
print('a',a, 'id is', id(a))
# a [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id is 2170081051584

#copy to b
b=a
print('b', b, 'id is', id(b))    # both a and b ids are same
# b [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id is 2170081051584

# in this type of copy, if we make any change in a or b that will
# reflect in other because of id location 

# to use shallow copy or deep copy, we need to import copy module

# *************

# now we copy a to c using copy module

import copy

# now clear b variable
b=''
print('b', b)    # both a and b ids are same
# b

b= copy.copy(a)

# check value and ids for a and b. 

print('a',a, 'id is', id(a))
# a [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id is 2170081051584

print('b', b, 'id is', id(b))    # both a and b ids are not same
# b [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id is 2170081207808


#Values are same ids are different

# now let us try to change a value 
a[1][2]=1000
a.append([10,11,12])

print('a', a, 'id is', id(a))
#a [[1, 2, 3], [4, 5, 1000], [7, 8, 9], [10, 11, 12]] id is 2170081051584

print('b', b, 'id is', id(b))
# b [[1, 2, 3], [4, 5, 1000], [7, 8, 9]] id is 2170081207808

# You can notice value edited in a as 1000 refleted in both a and b
# but appended values [10,11,12] in a is not added in b

# now let us try to change a value 
b[1][2]=100
b.append([13,14,15])

print('b', b, 'id is', id(b))
# b [[1, 2, 3], [4, 5, 100], [7, 8, 9], [13, 14, 15]] id is 2170081207808

print('a', a, 'id is', id(a))
# a [[1, 2, 3], [4, 5, 100], [7, 8, 9], [10, 11, 12]] id is 2170081051584

# You can notice value edited in b as 100 refleted in both a and b
# and appended values [13, 14, 15] in b is not added in a

# ***********

c=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('c', c, 'id of c is ', id(c))
# c [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id of c is  2250539246528

d=copy.deepcopy(c)
print('d', d, 'id of d is ', id(d))
# d [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id of d is  2250539246656

c[0][0]=10000
print('c', c, 'id of c is ', id(c))
# c [[10000, 2, 3], [4, 5, 6], [7, 8, 9]] id of c is  1486590878784
print('d', d, 'id of d is ', id(d))
# d [[1, 2, 3], [4, 5, 6], [7, 8, 9]] id of d is  2150057157888

d.append([10,100,1000])
print('d', d, 'id of d is ', id(d))
# d [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 100, 1000]] id of d is  2427795908032 
print('c', c, 'id of c is ', id(c))
# c [[10000, 2, 3], [4, 5, 6], [7, 8, 9]] id of c is  2299285447104

