# ******--    sys package

# ----------- 

import sys

print("The length of this argument is", len(sys.argv))  # returns how many arguments.
print("The length of this argument is", sys.argv[0])    # returns current file name as argument

a = sys.argv[1]
b= sys.argv[2]
c=int(a)+int(b) # change the value a and b in to integer because
                # getting values from commandline receives as string
print(c)

# When we start he programme as python temp.py 10 20

# output
# The length of this argument is 3
# The length of this argument is temp.py
# 30