# --list   []   list is a mutable object of list
# list work based on index, can accept duplicate value

listex = [1, 2, 3, 4, 5, 'python', 'p']
listex1 = ["c", "c#", "js"]
listex2 = [["c++", "R", "F#", "java", "cobol"], ["c", "c#", "js"]]  # this is called nested list
listex3 = [5, 3, 7, ["fas", "bee", "ray", "sha"]]
listex4 = [5, 3, 7, 150, 5, 89, 45, 325487, 215, 478, 124578, 120124587, 3526589741, 5456467867]

print(listex3[6:])  # slices back of the list
# output is [45, 325487, 215, 478, 124578, 120124587, 3526589741, 5456467867]

print(listex3[:6])  # slice front of the list
# output is [5, 3, 7, 150, 5, 89]

print(listex[2])  # output is 3
print(listex[5])  # output is python

listex.append(453)
print(listex)  # [1, 2, 3, 4, 5, 'python', 'p', 453]

listex.pop(1)  # 2 is removed from listex
print(listex)  # output is [1, 3, 4, 5, 'python', 'p', 453]

print(listex[-1])  # output is 453

temp = listex * 3
print(temp)
# output is [1, 3, 4, 5, 'python', 'p', 453, 1, 3, 4, 5, 'python', 'p', 453, 1, 3, 4, 5, 'python', 'p', 453]

for lst in listex:
    print(lst)

print(listex)
for lst in range(1, len(listex), 2):
    print(lst)
    # output is 1 3 5 -prints index of each selected element range from 1 from listex in step 2
    print(listex[lst])  # output is 3 5 p

temp = listex + listex1
print(temp)
# output is [1, 3, 4, 5, 'python', 'p', 453, 'c', 'c#', 'js']

temp = listex + listex1 + listex3
print(temp)
# output is [1, 3, 4, 5, 'python', 'p', 453, 'c', 'c#', 'js', 5, 3, 7, ['fas', 'bee', 'ray', 'sha']]

print(listex2)
# output is [['c++', 'R', 'F#', 'java', 'cobol'], ['c', 'c#', 'js']]

print(listex2[0][2])  # output is F#
print(listex2[1][1])  # output is C#

listex1[2] = "javascript"  # index value 2 "js" is replaced with "javascript"
print(listex1)
#  output is ['c', 'c#', 'javascript']

print(len(listex1))
# output is 3

print(len(listex2))  # listex2 is a nested list which has 2 list inside
# output is 2

print(max(listex4))  # This max method works only for numbers
# output is 5456467867

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)
# output is ['apple', 'banana', 'cherry']

############

# val1="fortran"
# print(val1)
# #output is fortran
# val2=list(val1)
# print(val2)
# #output is ['f', 'o', 'r', 't', 'r', 'a', 'n']

############

list1 = []

for i in range(10):
    list1.append(i)
print(list1)
# output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1.count(4)  # counts how many 4's are in list1

###########

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [5, 10.6, 1, 100, 200, 500]
list1.extend(list2)
print(list1)
# output is [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 10.6, 1, 100, 200, 500]

###########

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list1.insert(3, 'a')  # insert value 'a' after 3rd index value
print(list1)
# output is [0, 1, 2, 'a', 3, 4, 5, 6, 7, 8, 9]

list1.pop()  # last value in the list will be removed
print(list1)
# output is [0, 1, 2, 'a', 3, 4, 5, 6, 7, 8]

list1.pop(4)  # index 4 value removed
print(list1)
# output is [0, 1, 2, 'a', 4, 5, 6, 7, 8]

print(list1)
list1.remove(6)  # index 6 value removed
print(list1)

list1.reverse()  # all value values in the list is reversed
print(list1)
# output is [8, 7, 5, 4, 'a', 2, 1, 0]

list2 = [54, 12, 56, 6, 87, 86, 4, 56, 12, 36, 54, 89, 6, 454, 54, 54, 54, 54, 1]
list2.sort()
print(list2)
# output is [1, 4, 6, 6, 12, 12, 36, 54, 54, 54, 54, 54, 54, 56, 56, 86, 87, 89, 454]
