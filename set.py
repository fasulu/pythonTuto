# - set will not accept duplicate values
# set does not work based on index


list1 = {1, 2, 3, 4}  # curly brackets used to create set
list2 = set()  # another way to initialize set

list1.add(100)  # add adds a single value
print(list1)  # output is {1, 2, 3, 100, 4}

list1.remove(100)
print(list1)  # output is {1, 2, 3, 4}

list1.pop()  # first value in the set will be removed
print(list1)  # output is {2, 3, 4}

list1.clear()
print(list1)  # output is set()

list3 = {"apple", "banana", "cherry"}
list4 = {"google", "microsoft", "apple"}

list3.update(list4)  # update updates a set with another set, which ignore duplicate items
print(list3)  # output is {'cherry', 'apple', 'microsoft', 'banana', 'google'}

list5 = {100, 200, 300}
list6 = list5
# list5 and 6 shares the same memory location, if updated in list5 they will be updated in list6 automatically

list7 = list6.copy()
# list5 and list7 has same values, but if any one of the set is updated
# this will not affect other. They preserve their own values

# finding difference in set
a = {1, 2, 3, 4}
b = {1, 2, 5, 6}

print(a.difference(b))  # output is {3, 4}
print(b.difference(a))  # output is {5, 6}

# the above difference can also be done as following simple method
a = {1, 2, 3, 4}
b = {1, 2, 5, 6}

print(a - b)  # output is {3, 4}
print(b - a)  # output is {5, 6}

# difference_update in set
a = {1, 2, 3, 4}
b = {1, 2, 5, 6}

a.difference_update(b)
print(a, b)  # output is {3, 4} {1, 2, 5, 6}

# Union in set
a = {1, 2, 3, 4}
b = {1, 2, 5, 6}
print(a, b)  # output is {1, 2, 3, 4} {1, 2, 5, 6}

print(a.union(b))  # output is {1, 2, 3, 4, 5, 6}
# above can be done as below simple method
print(a | b)  # output is {1, 2, 3, 4, 5, 6}

# Intersection in set
a = {1, 2, 3, 4}
b = {1, 2, 5, 6}

print(a.intersection(b))  # output is {1, 2, 3, 4} {1, 2, 5, 6}
# above can be done as below simple method
print(a & b)  # output is {1, 2}

# isdisjoint in set - this always gives true or false

a = {1, 2, 3, 4}
b = {5, 6, 7}
c = {1, 5}

print(a.isdisjoint(b))  # result is True, because set a values and set b values are different
print(a.isdisjoint(c))  # result is False, because "1" is present in set a and set c

# issubset in set - this always gives true or false

a = {1, 2}
b = {1, 2, 5, 6}
c = {3, 9, 0}
print(a.issubset(b))  # result is True, because values "1, 2" are present in set a and set b
print(a.issubset(c))  # result is false, because values "1, 2" are not present in set a and set c

# issuperset in set - always returns true or false

a = {1, 2, 3, 4, 5}
b = {1, 2}

print(a.issuperset(b))  # result is true, because set b's values are present in set a
print(b.issuperset(a))  # result is false, because set a's values are not present in set b

# symmetric difference - this give values which are not common in both sets

a = {1, 2, 4, 5}
b = {1, 2, 6, 7, 9}

print(a.symmetric_difference(b))  # result is {4, 5, 6, 7, 9}
# the same code can be done by simple method also, as follows
print(a ^ b)  # result is {4, 5, 6, 7, 9}
