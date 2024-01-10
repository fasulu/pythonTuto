
# ************  append() vs extend() 

'''     
        To add a single entry to the end of a list, use the append() function.
        Syntax: list.append(item)
'''

str1=[1,2,3,4,5]
str2=[1,2,3,4,5]

str1.append(6)
print(str1)         # output is [1, 2, 3, 4, 5, 6]

str1.append([100,200])
print(str1)         # output is [1, 2, 3, 4, 5, 6, [100, 200]]

str1.append('world')
print(str1)         # output is [1, 2, 3, 4, 5, 6, [100, 200], 'world']

# as in above example, append() can accept any value given

'''     
        To add additional elements or an iterable to the end of a list, use the extend() function.
        Syntax: list.extend(string or object)
'''

# In extend(), it can't as above.
# extend() will accept only iterable objects like string, list, set etc

str2.extend('hello')
print(str2)         # [1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o']

str3 = [10,20]
str2.extend(str3)
print(str2)         # [1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o', 10, 20]

