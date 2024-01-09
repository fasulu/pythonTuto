
# ********list comprehension

# ********

list_new =[1,2,3,4,5]

list_square=[]

for i in list_new:
    sqrVal=i**2
    list_square.append(sqrVal)
print(list_square)

# output is [1, 4, 9, 16, 25]


#  The same logic can be done by following;
# this is called list comprehension

list_square_new = [sqrVal_new ** 2 for sqrVal_new in list_new]
print(list_square_new)

# output is [1, 4, 9, 16, 25]

# the following logic uses a condition <if>
list_square_new = [sqrVal_new ** 2 for sqrVal_new in list_new if sqrVal_new == 2]
print(list_square_new)

# output is [4]

# https://www.youtube.com/watch?v=27-PA9ZIfgk&list=PLIFRUdRwOM0_hcLruKbsHWnU5P2uLBgsp&index=71