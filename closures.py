# ************  closures

"""     
		A Closure in Python is a function object that remembers 
  		values in enclosing scopes even if they are not present in memory.
        
"""

# ********** First need to understand what is nested function and local variables.
				
#			As we can see innerFunction() can easily be accessed inside 
# 			the outerFunction body but not outside of its body. Hence, 
# 			here, innerFunction() is treated as a nested Function that 
# 			uses text as a non-local variable.

# this program to illustrate
# nested functions
def outerFunction(text):

	# the <text> is a non-local variable
 
	def innerFunction():
		print(text)			# Hey!

	innerFunction()

if __name__ == '__main__':
	outerFunction('Hey!')		
 
# ************  
 
# this program to illustrate 
# closures 
def outerFunction(text): 

	def innerFunction(): 
		print(text) 

	# Note we are returning function
	# WITHOUT parenthesis
	return innerFunction 

if __name__ == '__main__': 
	myFunction = outerFunction('Hey!') 
	myFunction() 

'''
the above programme, closures in Python help to invoke functions outside 
their scope. The function innerFunction has its scope only inside the
outerFunction. But with the use of Python closures, we can easily 
extend its scope to invoke a function outside its scope

'''
