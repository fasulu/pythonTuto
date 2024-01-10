# ********  map()

# ********  map(fun, iter)

def square(n):
    return (n ** 2)

# create a values by tuple
values = (1,2,3,4,5)

# pass values to square() function with map().
# result will be stored in a memory location as list
result = map(square,values)     

# this result can be retreived using print
print(list(result))

# output
# [1, 4, 9, 16, 25]


# Double all numbers using map and lambda
 
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# output
# [2, 4, 6, 8]

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
 
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# output
# [5, 7, 9]



# List of strings
lst = ['sky', 'moon', 'mars', 'sun']
 
# map() can listify the list of strings individually
test = list(map(list, lst))
print(test)

# output
# [['s', 'k', 'y'], ['m', 'o', 'o', 'n'], ['m', 'a', 'r', 's'], ['s', 'u', 'n']]


# Define a function that doubles even numbers and leaves odd numbers as is

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num
 
# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]
 
# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))
 
# Print the result
print(result)  # [1, 4, 3, 8, 5]

# output
# [1, 4, 3, 8, 5]