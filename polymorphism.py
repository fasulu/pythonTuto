# ******-- Polymorphism

# ----------- function overloading

class Demo():
  def sum(self,a=None, b=None, c=None):
    if a!=None and b!=None and c!=None:
      d=a+b+c
    elif a!=None and b!=None:
      d=a+b
    else:
      d=a
    print (d)

obj=Demo()
obj.sum(10,20,30)
obj.sum(10,20)
obj.sum(10)

# output
# 60
# 30
# 10

# ----------- function overriding

class Demo():
  def fun(self):
    print("Demo Class")
class DemoA(Demo):
  pass

obj=DemoA()
obj.fun()

# output
# Demo Class

# The above example output shows 'Demo Class' because child class is
# inherited base class.

class Demo():
  def fun(self):          # same function name
    print("Demo Class")
class DemoA(Demo):
  def fun(self):          # same function name
    print("DemoA Class")

obj=DemoA()
obj.fun()

# output
# DemoA Class

# Even child class inherited fun() funtion from Demo class 
# output shows "DemoA Class". The base class and child class
# has the same function (here it is fun()), the base class
# function is ignored.

# ******--Operator overloading

# ----------- 

class student():
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
  def __add__(self,temp):
    m1=self.m1 +temp.m1
    m2=self.m2 +temp.m2
    s3=student(m1,m2)
    return s3

s1=student(30,40)
s2=student(40,50)

s3=s1+s2
print(s3.m1)
print(s3.m2)

# output
# 70
# 90