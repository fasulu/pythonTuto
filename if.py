# a=int(input("enter a integer"))
# if a==4:
# 	print("four")
# elif a==5:
# 	print("five")
# elif a==6:
# 	print("six")
# else:
# print(f'Hi your are {a} year(s) old')


a = int(input("enter a value:- "))
b = int(input("enter b value:- "))
if a == 4:
    if a > b:
        print("yes a > b")
    else:
        print("No a < b")
else:
    print(f"terminated. {a} not equal to 4")

# *********** Ternary Operation
	
# expression_if_true if condition else expression_if_false

a = 'next'
result = True if a == 'next' else False
print(result)

# or use as follows;

a = 'next'
result = (a == 'next')
print(result)