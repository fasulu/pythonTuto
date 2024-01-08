# ******--User defined function

def myfuncx():
  print('welcome to python')

myfuncx()
# welcome to python

def myfuncy(a):
  print(a,', welcome to python')

myfuncy('ray')
# ray , welcome to python

def myfuncz(name='Child'):
  print(name,', welcome to python')

myfuncz()
# Child , welcome to python

def myfunczz(x):
  return x*100

returnVal = myfunczz(5)
print('Returned from function is',returnVal)
# Returned from function is 500