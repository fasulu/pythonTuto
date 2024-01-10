
# ************  Using else: in for and while loop 

'''     

'''

# Python 3.x program to check if an array consists  
# of even number 
def contains_even_number(l): 
    for ele in l: 
        if ele % 2 == 0: 
            print ("list contains an even number") 
            break
  
    # This else executes only if break is NEVER 
    # reached and loop terminated after all iterations. 
    else:      
        print ("list does not contain an even number") 
  
# Driver code 
print ("For List 1:") 
contains_even_number([1, 9, 8]) 
print (" \nFor List 2:") 
contains_even_number([1, 3, 5])

# output
'''
list contains an even number

For List 2:
list does not contain an even number
'''

#*************

for i in range(1, 4): 
    print(i) 
else:  # Executed because no break in for 
    print("No Break") 

# output
'''
1
2
3
No Break
'''

#************

count = 0
while (count < 1):     
    count = count+1
    print(count) 
    break
else: 
    print("No Break") 
    

