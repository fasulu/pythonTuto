# ************  logging()

"""     
		Logging is a means of tracking events that happen when some 
  software runs. Logging is important for software developing, 
  debugging, and running. If you don’t have any logging record and 
  your program crashes, there are very few chances that you detect 
  the cause of the problem. And if you detect the cause, it will 
  consume a lot of time. With logging, you can leave a trail of 
  breadcrumbs so that if something goes wrong, we can determine 
  the cause of the problem. 
        
"""

# ********** simple logging use

import logging

# logging.basicConfig(filename='errorLog.log',
#                     filemode='w',)

# log=logging.getLogger()
# log.setLevel(logging.DEBUG)
# log.debug('this is debug log')
# log.info('this is info log')
# log.error('this is error log')
# log.warning('this is warning log')
# log.critical('this is critical log')

# the error informations are saved in example.log under current directory

'''
Raising exceptions during logging can be useful in 
certain scenarios to indicate exceptional conditions or 
errors in your application. 

'''
# Create and configure logger
logging.basicConfig(filename="errorLog.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')

def perform_operation(value):
	if value < 0:
		raise ValueError("Invalid value: Value cannot be negative.")
	else:
		# Continue with normal execution
		logging.info("Operation performed successfully.")

try:
	input_value = int(input("Enter a value: "))
	perform_operation(input_value)
except ValueError as ve:
	logging.exception("Exception occurred: %s", str(ve))

# the error informations are saved in example.log under current directory

# ********** this following demonstrates using closures in logging

# logging.basicConfig(filename='errorLog.log',
# 					level=logging.INFO) 

# def logger(func): 
# 	def log_func(*args): 
# 		logging.info( 
# 			'Running "{}" with arguments {}'.format(func.__name__,
# 													args)) 
# 		print(func(*args)) 
		
# 	# Necessary for closure to
# 	# work (returning WITHOUT parenthesis) 
# 	return log_func			 

# def add(x, y): 
# 	return x+y 

# def sub(x, y): 
# 	return x-y 

# add_logger = logger(add) 
# sub_logger = logger(sub) 

# add_logger(3, 3) 
# add_logger(4, 5) 

# sub_logger(10, 5) 
# sub_logger(20, 10) 

# output
# Running "add" with arguments 6
# 9
# 5
# 10

# the log informations are saved in example.log under current directory

'''
An important thing to note here, is that we can get to know what 
variables are stored inside a Closure with the help of 
the __closure__ attribute that makes use of Cell Objects to 
store the variables of the Outer Function and because of this, 
the closure can use these variables even when the Outer Function 
is terminated.

'''
