# ************  partial()

"""     
        Partial functions allow us to fix a certain number of 
        arguments of a function and generate a new function.
        Syntax: partial(funtion, item(s))
"""

from functools import partial
from operator import mul


# *************
def partial_ex(str1, str2):
    data = str1 + str2
    return data

partial_func = partial(partial_ex, str1="Welcome ")
names = ["Sun", "Moon", "Mars"]
for x in names:
    print(partial_func(str2=x))

# output
'''
Welcome Sun
Welcome Moon
Welcome Mars
'''


# ************* Multiplication table using partial()

str1=int(input("Please enter a table number:-"))
def partial_ex(str1, str2):
    data = mul(str1, str2)
    # data = f"{str1}x{str2}=", mul(str1, str2)
    # data = "{}x{}=".format(str1,str2), mul(str1, str2)
    return data

partial_func = partial(partial_ex, str1)
num = [1,2,3,4,5]
for x in num:
    # print(partial_func(str2=x))
    # print(x,'x',str1,'=',partial_func(str2=x))
    print("{} x {} =".format(x,str1),partial_func(str2=x))

# output
'''
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
4 x 3 = 12
5 x 3 = 15
'''
# ***********

# A normal function
def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


# A partial function that calls f with
# a as 3, b as 1 and c as 4.
g = partial(f, 3, 1, 4)

# Calling g()
print(g(5))  # output is 3145

# *************


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c


# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)

# Calling partial function
print(add_part(3))  # output 312

input("Press a key to continue...")
