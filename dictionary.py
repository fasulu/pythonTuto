# Dictionary - It is like list, tuple and set one differenc is
# dictionary has key value pairs, ie each value is declared with its key
# dictionary is mutable
# dictionary does not allow duplicate keys

d = {}  # like set but without value becomes dictionary
print(type(d))  # result is <class 'dict'> 

d = {'a': 2, 'b': 5, 'c': 8, 'd': 4, 'e': 7, 'f': 8, 'g': 9, 'h': 11}
print(d)  # resulut is {'a': 2, 'b': 5, 'c': 8, 'd': 4, 'e': 7, 'f': 8, 'g': 9, 'h': 11}

print(d['d'])  # result is "4"
print(d.get('b'))  # result is "5"

# update dictionary value

d['c'] = 1  # change dictionary value c to 1
print(d)  # result is {'a': 2, 'b': 5, 'c': 1, 'd': 4, 'e': 7, 'f': 8, 'g': 9, 'h': 11}

del d['h']
print(d)  # result is {'a': 2, 'b': 5, 'c': 1, 'd': 4, 'e': 7, 'f': 8, 'g': 9}

d.pop('g')
print(d)  # result is {'a': 2, 'b': 5, 'c': 1, 'd': 4, 'e': 7, 'f': 8}


dict1={'a':1}
dict2={'b':2}
dict3={'c':3}

dict1.update(dict2)  # this will append dict2 in to dict1
print('dict1 value',dict1)  # dict1 value {'a': 1, 'b': 2}

dict4={**dict2, **dict3}  
print('dict4 value',dict4)  # dict4 value {'b': 2, 'c': 3}

# another way to do the above is 
dict4=dict2 | dict3     # dict4 value {'b': 2, 'c': 3}
print('dict2 value',dict2,'dict3 value',dict3)  # dict2 value {'b': 2} dict3 value {'c': 3}
print('dict4 value',dict4)  # dict4 value {'b': 2, 'c': 3}

###################

for i in d:
    print(d[i])

# result values are;
# 2
# 5
# 1
# 4
# 7
# 8

for i in d.values():
    print(i)

# result values are;
# 2
# 5
# 1
# 4
# 7
# 8

for i in d:
    print(i)

# result keys are;
# a
# b
# c
# d
# e
# f

for x, y in d.items():
    print(x, y)

# result values are;
# a 2
# b 5
# c 1
# d 4
# e 7
# f 8

for i in d:
    print(i, ':', d[i])

# result key and values are;
# a : 2
# b : 5
# c : 1
# d : 4
# e : 7
# f : 8

