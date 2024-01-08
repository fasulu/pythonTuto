# ******--Muttable and immutable difference

a=[1,2,3,4,5]
b=a
print('Memory location id is',id(a), 'value is', a)
print('Memory location id is', id(b), 'value is', b)

# Memory location id is 140355688046336 value is [1, 2, 3, 4, 5]
# Memory location id is 140355688046336 value is [1, 2, 3, 4, 5]

b[2]=100
print('Memory location id is',id(a), 'value is', a)
print('Memory location id is', id(b), 'value is', b)

# Memory location id is 140355688046336 value is [1, 2, 100, 4, 5]
# Memory location id is 140355688046336 value is [1, 2, 100, 4, 5]
# Values changed in the memory location, but location remains the same,
#  this is called muttable.

# ----------+

x=15
y=x

print('Memory location id is',id(x), 'value is x', x)
print('Memory location id is', id(y), 'value is y', y)

# Memory location id is 9764832 value is x 15
# Memory location id is 9764832 value is y 15

# Change value of y

y=1

print('Memory location id is',id(x), 'value is x', x)
print('Memory location id is', id(y), 'value is y', y)

# Now check value and memory id

# Memory location id is 9764832 value is x 15
# Memory location id is 9764384 value is y 1

# Memory location id of y is changed to new location
# this say this is a immutable 
