
# *********** Numbers:-

a=10
# type(a)	    int			shows type of a 

# b=3
# 
# a/b 		3.33333		with full result
# a//3		3 			only integer quotient value
# a%3		1			only reminder value
# a*b		30			multiplication
# a**b		1000        10*10*10 exponential
# 
# a =1+2j
# b=2+4j
# a+b		3+6j		complex numbers always has 'j' suffix
# 3+(5+4j)	8+4j        complex numbers add with integer
# 
# 3e5		    300000.0	3*10 power of 5

# *********** Operators:-

# /,*,-,+,//,**,%               arithmetic	
# ==,!=,>,> <=,=>               relational	gives always true or false result
# =, +=, -=, *=, /=, //=        assignment	
# OR, AND, NOT                  logical		
# AND(&), OR(|), xOR(^), compliment(~), left shift(<<), right shift(>>)     bitwise		
# in, not in	"o" in "computer" result is true                            membership	
# is, is not	id(a) is id(b)  identity		
# this checks memory locations of an variables.If the locations are same it gives true, if not gives false

# *********** Operation Priority

# ()			                    Parantheses
# +x, -x, ~x	                    Unary plus/minus, bitwise NO
# **			                    Exponential
# *, /, %, //	                    Multiply, divide, mod, floor division
# +, -		                        Addtion, substration
# >>,<<		                        Right and left shift
# &			                        Bitwise AND
# ^, |		                        Bitwise xOR and OR
# <=,<,>,>=	                        Comparison
# <, >, --, !=                      Equality
# =, %=, /=, //=, -=, +=, *=,**=	Assignment
# is, is not	                    Identity
# in, not in	                    Membership
# OR, AND, NOT	                    Logical

# *********** Strings:-

a="hello"
b='hello'
print(a)	# hello
print(b)	# hello
# 
a[1]		# gives e
b[4]		# gives o

a[1:2]	    # gives ell

a="it\'s him"		#it's him
b="it's him"		#it's him
c='it\'s him'		#it's him
d='it\'s "him"'	    #it's "him"

print(100 * a)		#prints "it\'s him" 100 times

a="c:\new"		    #prints "c:" one line and "ew" in the next line. 
				    #Meaning "\n" will be treated as new line command.
				
# To avoid the above problem use as;
a="c:\\new"		# The result is c:\new
a=r"c:\new"		# The result is c:\new

# *********** Type Casting:-

a=10			#a holds integer value 10
b=float(a)		#b holds float value 10.0

a="10"			# a holds string value 10
b=float(a)		# b holds float value 10.0

x=100			# x has integer value 100
y=str(x)		# y holds the 100 as string
type(y)			# the result is 'str'
print(y)		# gives 100 as string value

y=12.456
z=int(y)		# z holds int value of 12.456
print(z)		# the result is 12, drops all decimal values

# *** Cant convert alphabets and special characters to integer
# *** Can convert alphabets, numbers and special characters to string

# *********** Get User input:-

x=int(input("enter a number"))	
# This gets integer number as input, any character entered other than number will give as invalid(valueError)

x=str(input("enter a string"))
# This gets any character as input and stored as string

x=eval(input())
# If the input value entered number or arithmetic function, it will be evaluated and result is stored in x. If the input value is string it will throw as NameError as not defind
