

# ******--    Regular expression in python

# ----------- 

import re

text = " 3.10 Regular Expression in Python"

# ans = re.compile("Express")     # finds Express in the given string
# ans = re.compile("[a-z]")       # output is 'match='e''
# ans = re.compile("[a-z A-Z]")   # output is 'match='R''
# ans = re.compile("[A-Z a-z]")   # output same as 'match='R''
# ans = re.compile("[A-Z a-z 0-9]")   # output same as 'match='R''
# ans = re.compile("[A-Za-z0-9] +")   # output same as 'match='R''

# result = ans.search(text)

from re import match

# The following example demonstrates the use of the range of characters 
# to find out if a string starts with 'W' and is followed by an alphabet.

strings=["Welcome to Chayim", "weather forecast","Winston Churchill", "W.G.Grace","Wonders of India", "Water park"]

for string in strings:
    result = match("W[a-z]",string)
    print(result)

print(result)

# output
# <re.Match object; span=(0, 2), match='We'>
# None
# <re.Match object; span=(0, 2), match='Wi'>
# None
# <re.Match object; span=(0, 2), match='Wo'>
# <re.Match object; span=(0, 2), match='Wa'>
# <re.Match object; span=(0, 2), match='Wa'>

from re import search

# The re.search() function searches for a specified pattern anywhere in 
# the given string and stops the search on the first occurrence.

string = "Try to earn while you learn"

obj = search("earn", string)
print(obj)
print(obj.start(), obj.end(), obj.group())  

# output
# <re.Match object; span=(7, 11), match='earn'>
# 7 11 earn


from re import findall
# The object returns a list of all occurrences.

string = "Try to earn while you learn"

obj = findall("earn", string)
print(obj)

# output
['earn', 'earn']

# This can be used to get the list of words in a sentence. 
# The \W* pattern check which of the words do not have any vowels in them.

obj = findall(r"\w*", "Fly in the sky.")
print(obj)

for word in obj:
  obj = search(r"[aeiou]",word)
  if word!='' and obj==None:
    print(word)

# output
# ['Fly', '', 'in', '', 'the', '', 'sky', '', '']
# Fly
# sky

from re import finditer

# The re.finditer() function returns an iterator object of all 
# matches in the target string. For each matched group, 
# start and end positions can be obtained by span() attribute.

string = "Every day is to learn not only to earn"
it = finditer("earn", string)
for match in it:
    print(match.span())

#output
# (17, 21)
# (34, 38)

from re import split

string = "Try to earn while you learn."
words = split(r' ', string)
print(words)

# output
# ['Try', 'to', 'earn', 'while', 'you', 'learn.']

from re import *

# The re.compile() function returns a pattern object which can be 
# repeatedly used in different regex functions. In the following example, 
# a string 'is' is compiled to get a pattern object and is subjected 
# to the search() method.

pattern = compile(r'[aeiou]')
string = "Flat is better than nested. Sparse is better than dense."
words = split(r' ', string) 
for word in words:
    print(word, pattern.match(word))

# output
# Flat None
# is <re.Match object; span=(0, 1), match='i'>
# better None
# than None
# nested. None
# Sparse None
# is <re.Match object; span=(0, 1), match='i'>
# better None
# than None
# dense. None

from re import *

# Can be used in searching for words having vowels

pattern = compile(r'[aeiou]')
string = "Flat is better than nested. Sparse is better than dense."

for word in words:
    print(word, pattern.search(word))

# output
# Flat <re.Match object; span=(2, 3), match='a'>
# is <re.Match object; span=(0, 1), match='i'>
# better <re.Match object; span=(1, 2), match='e'>
# than <re.Match object; span=(2, 3), match='a'>
# nested. <re.Match object; span=(1, 2), match='e'>
# Sparse <re.Match object; span=(2, 3), match='a'>
# is <re.Match object; span=(0, 1), match='i'>
# better <re.Match object; span=(1, 2), match='e'>
# than <re.Match object; span=(2, 3), match='a'>
# dense. <re.Match object; span=(1, 2), match='e'>


import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# output
# YES! We have a match!

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# output
# None

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# output
# []
# No match

# Find email using regex

regex = re.compile(r'([A-Za-z0-9]+[.-_])*([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# emails = ["name.surname@gmail.com"
# "anonymous123@yahoo.co.uk"
# "anonymous123@...uk"
# "...@domain.us"]

def isValid(email):
    if re.fullmatch(regex, email):
        print("Valid email")
    else:
        print("Invalid email")

isValid("name.surname@gmail.com")
isValid("anonymous.A123@co.uk")
isValid("an_anonymous123@yahoo.co.uk")
isValid("an_ano.nymous123@yahoo.co.uk")
isValid("an-anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")

# output
# Valid email
# Valid email
# Valid email
# Valid email
# Invalid email
# Invalid email
# Invalid email

# Find all email addresses from a document

txtDoc = "What is regular expression? want to know contact regex_school@www3.com, Users1@gmail.de " \
       "dayan@asda-asasa.com.lo,fuki.lastName@myDomain.com, darul-isa.lastName@domain.co.my"
match = re.findall(r'[\w\.-]+@[\w\.-]+', txtDoc)
for i in match:
    print(i)

# output
# regex_school@www3.com
# Users1@gmail.de
# dayan@asda-asasa.com.lo
# fuki.lastName@myDomain.com
# darul-isa.lastName@domain.co.my