# ----------- string built-in methods

str='hello woRld'
print(str.capitalize())     # Hello World. Changes to camal case
print(str.center(25))       # hello world. leaves 8 character space in and 8 character back
print(str.casefold())       # hello world - Change upper to lower
print(str.count('ll'))      # 1 - gives how many 'll' are in str
print(str.endswith('ld'))   # checks is the sring ends with 'ld', returns true or false
print('hello\tworld'.expandtabs(10))   # hello     world, increases 10 tabs space between hello and world
str='The Python extension automatically detects existing conda environments'
print(str.find('xi'))       # 44,  finds first occurence of 'xi' letters. If not found returns -1, means not found
print(str.index('zi'))      # throws 'ValueError: substring not found'. If given is not found throws error

print('hello 123'.isalpha())  # false, it contains numbers also
print('hello'.isalpha())  # true, it contains only alphabets
print('hello123'.isalnum())  # true, it contains numbers also
print('3434534'.isdigit())  # true, it contains only digits
print('  '.isspace())  # true, it contains only space
print('hello agent77  ╬'.isascii())  # true, it contains only space, number, alphabets and ascii character etc
print('systemOut'.isidentifier())     # return true, string starts with a alphabet
print('1systemOut'.isidentifier())     # return false, string starts with a number. All identifiers starts with alphabet
print('hello123'.islower())           # true, contains lowercase
print('\nDaddy Cool'.isprintable())   # false, because '\n' is not a printable character, it is a newline identifier
print('Daddy Cool'.istitle())       # true, because it contains all words starts with capital letters
print('Daddy Cool'.upper())       # changes lowercase to uppecase
print('Daddy Cool'.lower())       # changes uppercase to lowercase
print('Daddy Cool'.isupper())       # false, all not in uppercase
print('daddy cool'.islower())       # true, all are in lowercase

print('Daddy Cool'.upper())       # changes lowercase to uppecase
print('Daddy Cool'.lower())       # changes uppercase to lowercase
print('Daddy Cool'.replace(' ','-'))       # Daddy-Cool
print('Daddy Cool'.split())                 # ['Daddy', 'Cool']
print('Daddy-Cool'.split('-'))              # ['Daddy', 'Cool']
print('Daddy-Cool'.strip('-Cool'))              # Daddy
print(str.join(['a','c','b']))      # acb
str='abcDFdxcfsSDHSA'
print(min(str))     # returns 'A', as per ascii table 'A' value is 65 and 'a' is 61
print(max(str))         # returns 'x', as per ascii table 'x' value is 120 and 'S' is 83
str='youtube.com'
print(str.title())    # Youtube.Com

