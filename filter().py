
# ************  filter() 

'''     
        The filter() method filters the given sequence with 
        the help of a function that tests each element in the 
        sequence to be true or not. 
        Syntax: filter(function, sequence)
'''

num=[1,2,3,4,5,6,7,8,9,10]

def filterNum(data):
    if data % 2 == 0:
        return True
    else:
        return False

result = filter(filterNum, num) # if return value is True, filter stores current num value to result

print('The filtered letters are:')
for x in result:
    print(x)
    
# output
'''
The filtered letters are:
2
4
6
8
10
'''

# ************

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
 
sequence = ['m', 'o', 'o', 'j', 'n', 'x', 'i', 'z']
 
# using filter function
filtered = filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)

# output
'''
The filtered letters are:
o
o
i
'''

# *************

# Here, the lambda function to filter out the odd and even numbers from a list.

# a list contains both even and odd numbers. 
data = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, data)
print(list(result))

# output
# [1, 3, 5, 13]

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, data)
print(list(result))

# output
# [0, 2, 8]

'''
 The filter() function is used to apply this function to each 
 element of the numbers list, and the lambda function is used 
 to iterate over each element of the list before applying the 
 condition. In this way, it can perform additional operations on 
 each element before applying the condition.
'''

# Define a function to check 
# if a number is a multiple of 3
def is_multiple_of_3(num):
	return num % 3 == 0


# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result)

# output
# [3, 6, 9]
