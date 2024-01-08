# ******--break

i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break           # break: Breaks whole loop and comes out.
print("loop terminated") 

# ******--continue

i=0
while i<10:
    i+=1
    if i==5:
        continue        # continue: continue will diverts the loop to parent and avoid printing i
    print(i)

# ******--pass

i=0 
for i in range(10):
	if i==5:
		pass		# pass: this will pass certain code of line without doing nothing
	else:
		print(f"current value is {i}")