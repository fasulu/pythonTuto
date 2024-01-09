

# ********  *args and **kwargs

# ********  


def myFun(*args):
    for arg in args:
        print(arg) 
 
myFun('Hello', 'Welcome', 'to', 'python')
# Output;

# Hello
# Welcome
# to
# python

def myFun(arg1, *args):
	print("First argument :", arg1)
	for arg in args:
		print("Next argument through *args :", arg)


myFun('Hello', 'Welcome', 'to', 'python')

# Output;

# First argument : Hello
# Next argument through *args : Welcome
# Next argument through *args : to
# Next argument through *args : python

def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))    # 1st %s taken as key and 2nd %s taken as value
		# print(key, "==" ,value)             # this syntax is equivalent to the above


# Driver code
myFun(first='Welcome', mid='to', last='python')

# Output;

# first == Welcome
# mid == to
# last == python

def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Welcome', mid='to', last='python')

# Output;

# first == Welcome
# mid == to
# last == python


def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Welcome", "to", "python")
myFun(*args)

kwargs = {"arg1": "Welcome", "arg2": "to", "arg3": "python"}
myFun(**kwargs)

# Output;

# arg1: Welcome
# arg2: to
# arg3: python
# arg1: Welcome
# arg2: to
# arg3: python


def myFun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('Welcome', 'to', 'python', first="Welcome", mid="to", last="python")

# Output;

# args:  ('Welcome', 'to', 'python')
# kwargs:  {'first': 'Welcome', 'mid': 'to', 'last': 'python'}


# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, *args):
		# access args index like array does
		self.speed = args[0]
		self.color = args[1]


# creating objects of car class
toyota = car(200, 'red')
nissan = car(250, 'black')
honda = car(190, 'white')

# printing the color and speed of the cars
print(toyota.color)
print(nissan.speed)

# Output;

# red
# 250

# defining car class
class car():
	# args receives unlimited no. of arguments as an array
	def __init__(self, **kwargs):
		# access args index like array does
		self.speed = kwargs['s']
		self.color = kwargs['c']


# creating objects of car class
toyota = car(s=200, c='red')
nissan = car(s=250, c='black')
honda = car(s=190, c='white')

# printing the color and speed of cars
print(toyota.color)
print(nissan.speed)

# Output;

# red
# 250