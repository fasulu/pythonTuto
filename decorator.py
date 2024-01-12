# ************  decorators

"""     
		Decorators are a very powerful and useful tool in Python 
  since it allows programmers to modify the behaviour of a function 
  or class. Decorators allow us to wrap another function in order 
  to extend the behaviour of the wrapped function, without 
  permanently modifying it. But before diving deep into decorators 
  let us understand some concepts that will come in handy in 
  learning the decorators.
        
"""

# ****************** Treating the functions as objects. 

# this program to illustrate functions 
# can be treated as objects 
def shout(text): 
	return text.upper() 

print(shout('Hello')) 

yell = shout 

print(yell('Hello')) 

# output
'''
HELLO
HELLO
'''

# ****************** Passing the function as an argument 

# this program to illustrate functions 
# can be passed as arguments to other functions 

def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("Hi, I am created by a function passed as an argument.") 
	print (greeting) 

greet(shout) 
greet(whisper) 

# output

'''
HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT.
hi, i am created by a function passed as an argument.

'''

# ****************** Returning functions from another function. 

# this program to illustrate functions 
# Functions can return another function 

def create_adder(x): 
	print('Value of x is',x)				# Value of x is 15
	def adder(y): 
		print('Value of y is',y)			# Value of y is 10
		print('Value of x+y is',x+y)		# Value of x+y is 25
		return x+y 
	return adder 

add_15 = create_adder(15) 

print('Value of add_15(10) is',add_15(10)) 	#Value of add_15(10) is 25

'''
		As stated above examples the decorators are used to modify 
		the behaviour of function or class. In Decorators, 
		functions are taken as the argument into another function and 
		then called inside the wrapper function.

'''

def hello_decorator(func):

	# inner1 is a Wrapper function in 
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used()

# output

'''
Hello, this is before function execution
This is inside the function !!
This is after function execution

'''

# ****************** this programme easily find out the 
# 						execution time of a function using a decorator.
# 						defining a decorator

# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,
	# if function takes any arguments,
	# can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__, end - begin)

	return inner1

# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time
	# so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)

# output

'''
Hello, this is before function execution
This is inside the function !!
This is after function execution
3628800
Total time taken in :  factorial 2.0074660778045654

'''

# ****************** the following example will explain how a function returns a value


def hello_decorator(func):
	def inner1(*args, **kwargs):
		
		print("before Execution")
		
		# getting the returned value
		returned_value = func(*args, **kwargs)
		print("after Execution")
		
		# returning the value to the original frame
		return returned_value
		
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

# output

'''
before Execution
Inside the function
after Execution
Sum = 3

'''