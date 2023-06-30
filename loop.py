# --for

a = "Good"
for i in a:
    print(i)

# for i in range(len(a)):
# 	print(f"\n{i}")			#prints after finding length of variable a

# for i in range(1,10):
# 	print(f"\n{i}")			#prints starting from 1 to 9 exits at 10

# for i in range(1,11,2):	# range(1,11,2): range start from 1 to 1 by step 2
# 	print(f"\n{i}")			#prints starting from 1 to 9 even numbers exits at 11

# for i in range(1,11,1):
# 	print(f"\n{i}")			#prints starting from 1 to 9 odd numbers exits at 11


# --break

# i=0
# while i<10:
#     print(i)
#     i+=1
#     if i==5:
#         break           # break: Breaks whole loop and comes out.
# print("loop terminated") 

#  --continue

# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue        # continue: continue will diverts the loop to parent and avoid printing i
#     print(i)

# --pass

i = 0
for i in range(10):
    if i == 5:
        pass  # pass: this will pass certain code of line without doing nothing
    else:
        print(f"current value is {i}, line 47")
