# ******--    iterators package

# ----------- 

# Normal iteration will done by few functions for <for>

myData=['A','B','C','D','E']
for i in myData:
    print(i)

# create <iter> for iteration and 
# use <next> to get next value inthe iteration

myList=iter(myData)

print(myList)

# output is <list_iterator object at 0x000001B76FADEE60>
# myList stored in this memory location

# to get value from myList 

print(next(myList)) # output is A
print(next(myList)) # output is B
print(next(myList)) # output is C

# another way to get myList value is
print(myList.__next__()) # output is D
print(myList.__next__()) # output is E

