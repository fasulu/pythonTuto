# ******--File handling

f = open("/home/fasulu/PycharmProjects/pythonTutorial.txt", "r")

print("Name of the file ", f.name)
print("Mode of the file ", f.mode)
print("Is the file close", f.closed)
f.close()
print("Is the file close", f.closed)


# ******--File handling, read and write in file

# r+ is read and write mode

f= open("/home/fasulu/PycharmProjects/test.txt", "r")
print("Name of the file ", f.name)
print("Mode of the file ", f.mode)

dataStr=f.read()    # reads whole file
dataStr=f.read(25)  # reads first 25 character in the file

print(dataStr)
f.close()
print("Is the file close", f.closed)

f= open("/home/fasulu/PycharmProjects/test.txt", "r+")
print("Mode of the file ", f.mode)
# f.write("lskdajflsadkfj") # IMPORTANT will overwrites the file(which will delete the previous text in the file)
dataStr=f.read()
print(dataStr)
f.close()
print("Is the file close", f.closed)


# ******--File handling, file manipulation

# ----------- Open a text file

# r+ is read and write mode

f= open("/home/fasulu/PycharmProjects/test.txt", "r+")
for lines in f.readlines():
  print(lines)              # prints each line from the file one by one
f.close()

# ----------- Count total lines

f= open("/home/fasulu/PycharmProjects/test.txt", "r+")
dataStr=len(f.readlines())   # counts total lines
print("\n",dataStr)
f.close()

# ----------- Split a line word by word in to a list

f=open("/home/fasulu/PycharmProjects/language.txt", "r")
for dataStr in f.readlines():
  splitedData=dataStr.split()   # will split and store in a list
  print(splitedData)

# output
['Year', 'Name', 'Developer', 'Company', 'Predecessor']
['1960', 'COBOL61', 'CODASYL', 'FLOW-MATIC', 'COMTRAN']
['1962', 'FORTRAN-IV', 'IBM', 'IBM', 'FORTRAN', 'II']
['1964', 'BASIC', 'John-Thomas', 'IBM', 'FORTRAN', 'II']
['1972', 'SQL', 'IBM', 'Ingres', 'ALPHA-Quel']
['1983', 'Objective-C', 'Brad', 'Smalltalk', 'C']
['1991', 'VB', 'AlanCooper', 'Microsoft', 'QuickBASIC']
['1990', 'Z-shell', 'Falstad', 'Princeton', 'ksh']
['1995', 'Java', 'Gosling', 'Sun', 'C-CC++']
['1995', 'Ruby', 'Matsumoto', 'Smalltalk', 'Perl']
['1972', 'C', 'Ritchie', 'Microsoft', 'ALGOL', '68']
['1995', 'JavaScript', 'Brendan', 'Netscape', 'LiveScript']
['1983', 'TurboPascal', 'Hejlsberg', 'ALGOL', 'Pascal']
['1991', 'Python', 'Guido', 'Person', 'Perl-C']
['2000', 'C#', 'Hejlsberg', 'Microsoft', 'C-Java']
['2011', 'Kotlin', 'JetBrains', 'Sun', 'Java-C#']
['2005', 'F#', 'Syme', 'Microsoft', 'C#']
['2012', 'TypeScript', 'Hejlsberg', 'Microsoft', 'JS-CoffeeScript']

# ----------- Split a text file line by line and show in list

languages=[]
f=open("/home/fasulu/PycharmProjects/language.txt", "r")
for dataStr in f.readlines():
  splitedData=dataStr.split()   # will split and store in a list
  languages.append([splitedData[0],splitedData[1],splitedData[2],splitedData[3]])
print(languages)

f.close()

# Output
# [
#    ['Year', 'Name', 'Developer', 'Company'], 
#    ['1960', 'COBOL61', 'CODASYL', 'FLOW-MATIC'], 
#    ['1962', 'FORTRAN-IV', 'IBM', 'IBM'], 
#    ['1964', 'BASIC', 'John-Thomas', 'IBM'], 
#    ['1972', 'SQL', 'IBM', 'Ingres'], 
#    ['1983', 'Objective-C', 'Brad', 'Smalltalk'], 
#    ['1991', 'VB', 'AlanCooper', 'Microsoft'], 
#    ['1990', 'Z-shell', 'Falstad', 'Princeton'], 
#    ['1995', 'Java', 'Gosling', 'Sun'], 
#    ['1995', 'Ruby', 'Matsumoto', 'Smalltalk'], 
#    ['1972', 'C', 'Ritchie', 'Microsoft'], 
#    ['1995', 'JavaScript', 'Brendan', 'Netscape'], 
#    ['1983', 'TurboPascal', 'Hejlsberg', 'ALGOL'], 
#    ['1991', 'Python', 'Guido', 'Person'], 
#    ['2000', 'C#', 'Hejlsberg', 'Microsoft'], 
#    ['2011', 'Kotlin', 'JetBrains', 'Sun'], 
#    ['2005', 'F#', 'Syme', 'Microsoft'], 
#    ['2012', 'TypeScript', 'Hejlsberg', 'Microsoft']
#  ]

# -----------Find a string in a text file

f=open("/home/fasulu/PycharmProjects/language.txt", "r")
count=0
lines=[]
searchStr=input("Please enter your search string:- ")
for line in f.readlines():
  count+=1
  if searchStr in line:
    print("Your string found in line number", count)    ## print line where the string found
    lines.append(count)
print("Your string found in line number(s)", lines)     ## prints all line numbers where the string found
f.close()

# Output
# Please enter your search string:- 1983
# Your string found in line number 6
# Your string found in line number 13
# Your string found in line number(s) [6, 13]