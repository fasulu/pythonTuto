# ********yield function

# ********generator using yield function

def demo():
    n= 1
    while n<= 10:
        val = n*n
        n+=1
        # yield val       # here we can't use return to run as iteration
        return val      # try to know the result of return in this programme
a=demo()
for i in a:
    print(i)
    
# output
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

# If we run the above logic with <return> 
# and without <yield>, the output will be;

# Traceback (most recent call last):
#   File "e:\Python\temp.py", line 14, in <module>
#     for i in a:
# TypeError: 'int' object is not iterable