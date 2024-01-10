
# ************  random()

'''   random module generates random numbers in Python. 
    These are pseudo-random numbers means they are not truly random.

    This module can be used to perform random actions such as
    generating random numbers, printing random a value for a 
    list or string, etc. It is an in-built function in Python.
        
'''

import random as rnd

mixed=[1,'e',4,'xmas','j', 9,'mat',11,45,'moon']

mixSelected=rnd.choice(mixed)
print('selected number',mixSelected)   # output will be any one from the given mixed list

data=[1,2,3,4,5,6,7,8,0]

selected=rnd.choice(data)
print('selected number',selected)   # output will be any one from the given data list

word = "pneumonoultramicroscopicsilicovolcanoconiosis"
print(rnd.choice(word))   # output will be one charcter from variable word

rnd.shuffle(data)
print('Shuffled data is', data) # output will be 'Shuffled data is [8, 4, 5, 2, 1, 7, 0, 6, 3]'

selected=rnd.random()               # generate random number
print('random number', selected)    # output will be floating number

# to get interger number from the <selected> variable
print('random number', int(selected*10)) 

# to use builtin function to create integer random number
# prints any integer between 1 and 100
print('used builtin function randinit', rnd.randint(1,100))

# prints any integer with 3 digits or 4 digits
print('used builtin function randinit', rnd.randint(100,1000))
print('used builtin function randinit', rnd.randint(1000,10000))

# randrange(start, end, step) here 15 is step
print('used builtin function randrange', rnd.randrange(100,1000, 15)) 

# sample(variable, number of choice)
print('used builtin function sample', rnd.sample(mixed, 3))  # output is ['e', 'xmas', 11]

