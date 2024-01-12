# ************  heapq()

"""     
        The property of this data structure in Python is that each time 
        the smallest heap element is popped(min-heap). Whenever elements 
        are pushed or popped, heap structure is maintained. The heap[0] 
        element also returns the smallest element each time.
        Syntax : any(List, Dictionary, Tuple, set, etc) 
"""

# ****************** 

import heapq

# initializing list
listA=[1,23,10,100,102,1000,5,265]
listB = [5, 7, 9, 4, 3]

# original listA
print("The original listA", listA)

# original listB
print("The original listB", listB)

result=heapq.nlargest(3,listA)
print(result)						# [1000, 265, 102]

# ****************** 

result=heapq.nsmallest(2,listA)
print(result)						# [1, 5]

# ****************** 

# using heapify to convert list into heap
heapq.heapify(listA)

# printing created heap
print("The created heap is : ", end="")
print(list(listA))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(listA, 4)

# printing modified heap
print("The modified heap after push is : ", end="")
print(list(listA))

# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(listA))

# ****************** 

# initializing list 1
li1 = [5, 1, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# output
'''
The popped item using heappushpop() is : 1
The popped item using heapreplace() is : 3
'''

# ****************** 

# Initialize a list with some values
values = [5, 1, 3, 7, 4, 2]

# Convert the list into a heap
heapq.heapify(values)

# Print the heap
print("Heap:", values)

# Add a new value to the heap
heapq.heappush(values, 6)

# Print the updated heap
print("Heap after push:", values)

# Remove and return the smallest element from the heap
smallest = heapq.heappop(values)

# Print the smallest element and the updated heap
print("Smallest element:", smallest)
print("Heap after pop:", values)

# Get the n smallest elements from the heap
n_smallest = heapq.nsmallest(3, values)

# Print the n smallest elements
print("Smallest 3 elements:", n_smallest)

# Get the n largest elements from the heap
n_largest = heapq.nlargest(2, values)

# Print the n largest elements
print("Largest 2 elements:", n_largest)

# output
'''
Heap: [1, 4, 2, 7, 5, 3]
Heap after push: [1, 4, 2, 7, 5, 3, 6]
Smallest element: 1
Heap after pop: [2, 4, 3, 7, 5, 6]
Smallest 3 elements: [2, 3, 4]
Largest 2 elements: [7, 6]
'''
