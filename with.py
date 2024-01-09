
# ********<with> statement

# ********  <with> works like <try:... finally:>

fs= open(r'E:\Python\slicing.py','r')   # <r> at the start of path says it is raw string(contains .\:)
data=fs.read()
print(data)
fs.close()

# When you call the open() function using the with statement, 
# the file closes automatically after you’ve processed the file.

with open(r'E:\Python\slicing.py','r') as fs:
    contents=fs.read()
print(contents)

# Under the hood, the with statement replaces this kind of try-catch block:
file= open(r'E:\Python\slicing.py','r')
try:
    file.read()
finally:
    file.close()