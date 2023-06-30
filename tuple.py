# -- Tuple    ()   tuple is the immutable, read-only list of object
# All like slice, max, min and add can be done except altering the tuple list
# tuple works based on index, can accept dulicate value

list1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
list2 = (5, 10.6, 1, 100, 200, 500)

print(list1)
# output is (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# to add in tuple object

list1 = list1 + (100,)
print(list1)
# output is (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100)

# to delete a tuple

del list1
# print(list1)    # list1 tuple is deleted
# output is NameError: name 'list1' is not defined

# change a list into tuple

list1 = [1, 5, 4, 6, 8, 75, 897]
changedtotuple = tuple(list1)
print(type(changedtotuple))  # output is <class 'tuple'>
