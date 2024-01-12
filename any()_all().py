
# ************  any() and all()

"""     
        any() function returns True if any of the elements of a given 
        iterable( List, Dictionary, Tuple, set, etc) are True else 
        it returns False.
        Syntax : any(List, Dictionary, Tuple, set, etc) 
"""

# ****************** with string

# Non-Empty String
strA = "Hi There!"
# return True
print(any(strA))

# Non-Empty String
strA = "000"
# return True
print(any(strA))

# Empty string
# returns False
strA = ""
print(any(strA))


# ****************** with list

listA = [True,True,False] 
# returns True since at least one element in the listA
print(any(listA))

# All elements of list are True
listA = [4, 5, 1]
print(any(listA))
 
# All elements of list are False
listA = [0, 0, False]
print(any(listA))
 
# Some elements of list are
# True while others are False
# returns True
l = [1, 0, 6, 7, False]
print(any(l))
 
# Empty list returns False
l = []
print(any(listA))


# ****************** with tuple

# All elements of tuple are True
tupleA = (2, 4, 6)
print(any(tupleA))
 
# All elements of tuple are False
tupleA = (0, False, False)
print(any(tupleA))
 
# Some elements of tuple are True while
# others are False
# return True
tupleA = (5, 0, 3, 1, False)
print(any(tupleA))
 
# Empty tuple
# returns False
tupleA = ()
print(any(tupleA))


# ****************** with set

# All elements of set are True
setA = { 1, 1, 3}
print(any(setA))
 
# All elements of set are False
setA = { 0, 0, False}
print(any(setA))
 
# Some elements of set are True while others are False
# returns True
setA = { 1, 2, 0, 8, False}
print(any(setA))
 
# Empty set
# returns False
setA = {}
print(any(setA))


# ****************** with dict

# All keys of dictionary are true
dictA = {1: "Hello", 2: "Hi"}
print(any(dictA))

# All keys of dictionary are false
dictA = {0: "Hello", False: "Hi"}
print(any(dictA))

# Some keys of dictionary
# are true while others are false
# returns True
dictA = {0: "Salut", 1: "Hello", 2: "Hi"}
print(any(dictA))

# Empty dictionary
# returns False
dictA = {}
print(any(dictA))

# ****************** any() with condition

# this code to demonstrate working of any()
# To Check if any element in list satisfies a condition

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : ", test_list)

# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list)

# Printing result
print("Does any element satisfy specified condition ? : ", res)

# output
'''
The original list : [4, 5, 8, 9, 10, 17]
Does any element satisfy specified condition ? : True

'''

# ****************** any() with For lop

# this function gives same result as built-in any() function
def my_any(list_x):
	for item in list_x:
		if item:
			return True
	return False

x = [4, 5, 8, 9, 10, 17]		# will return True
# x = [0,0]			# will return False
print(my_any(x))			# True
