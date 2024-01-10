# ************  assert keyword

"""     
        In simpler terms, the assertion is the boolean expression 
        that checks if the statement is True or False.
        Syntax : assert condition, error_message(optional) 
"""

# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0
print(a / b)

# output
'''
The value of a / b is : 
Traceback (most recent call last):
  File "e:\Python\temp.py", line 15, in <module>
    assert b != 0
AssertionError

'''

# Python 3 code to demonstrate
# working of assert
 
# initializing number
a = 4
b = 0
 
# using assert to check for 0
print("The value of a / b is : ")
assert b != 0, "Zero Division Error"
print(a / b)

# output
'''
AssertionError: Zero Division Error

'''

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
	# Assertion to check that the length and width are positive
	assert length > 0 and width > 0, "Length and width"+ \
				"must be positive"
	# Calculation of the area
	area = length * width
	# Return statement
	return area


# Calling the function with positive inputs
area1 = calculate_rectangle_area(5, 6)
print("Area of rectangle with length 5 and width 6 is", area1)

# Calling the function with negative inputs
area2 = calculate_rectangle_area(-5, 6)
print("Area of rectangle with length -5 and width 6 is", area2)

# output
'''
AssertionError: Length and widthmust be positive

'''

# Initializing variables
x = 10
y = 20

# Asserting a boolean condition
assert x < y

# Printing the values of x and y
print("x =", x)
print("y =", y)

# output
'''
x = 10
y = 20

'''



# Initializing variables
a = "hello"
b = 42
 
# Asserting the type of a variable
assert type(a) == str
assert type(b) == int
 
# Printing the values of a and b
print("a =", a)
print("b =", b)

# output
'''
a = hello
b = 42

'''
