# ******--class - OOP

# ----------- 

# By convention, userdefined classes start with capital lettes
class Demo:
  print("class method")
  a=10
  b=20
  print(a)

# now use the above class Demo, create a object as obj as follows;
  
obj=Demo()
print(obj.b)

# Output
# class method
# 10
# 20

# ----------- 

class Demo:
  print("class method")
  def example(self, a,b):   # create function example
    c=a+b
    print(c)
obj=Demo()
obj.example(10,20)  # Call example function

# Output
# class method
# 30

# ----------- use of <self> in a function

class Demo:
  print("class method")
  x=100
  def example(self, a,b):   # create function example
    c=a+b*self.x            # the variable <x> is declared outside example funtion, which can be accessed by placing <self> in funtion as argument and using the variable <x> as <self.x> inside funtion

    print(c)
obj=Demo()
obj.example(10,20)  # Call example function

# Output
# class method
# 2010

# ----------- returning a result from a function

class Demo:
  x=154
  def example(self, a,b):   # create function example
    c=a+b*self.x            # the variable <x> is declared outside example funtion, which can be accessed by placing <self> in funtion as argument and using the variable <x> as <self.x> inside funtion
    return c

obj=Demo()
returnedVal = obj.example(10,20)  # Call example function
print("Returned value is",returnedVal)

# Output
# Returned value is 3090


# ******--class - OOP - Constructor

# ----------- Create and use the constructor

class Demo:
  print("Demo class")

  # Create a constructor
  def __init__(self):
    self.name="Fuji"
    self.age= 15

  # Use the constructor
  def display(self):
    print("My name is", self.name, "and my age is", self.age)

# Pass value to the constructor
obj= Demo()
# Call the constructor to print the value
obj.display()

# Output
# Demo class
# My name is Fuji and my age is 15


# ----------- Create and passing value to the constructor

class Demo:
  print("Demo class")

  # Create a constructor
  def __init__(self,name, age):
    self.name=name
    self.age=age

  # Use the constructor
  def display(self):
    print("My name is", self.name, "and my age is", self.age)

# Pass value to the constructor
obj= Demo("Biji", 95)
# Call the constructor to print the value
obj.display()

# Output
# Demo class
# My name is Biji and my age is 95

# ******--class - OOP - Inheritance

# ----------- Single Inheritance - Create Dad as base class  

class Dad():  # base class
  f_name="Apple"
  f_type="Big Fruit"

class Son(Dad): # child class, which inherits Dad class
  s_name="Plum"
  s_type="Smal Fruit"

# Accessing Dad class
print("Dad name is", Dad.f_name, "and type is", Dad.f_type)

# Output
# Dad name is Apple and type is Big Fruit

# Accessing Dad class through inheritance
# To access Dad class create object using Son class

obj=Son()
print("Dad name is", obj.f_name, "and type is", obj.f_type)
print("Son name is", obj.s_name, "and type is", obj.s_type)

# Output
# Dad name is Apple and type is Big Fruit
# Son name is Plum and type is Smal Fruit


# ******--class - OOP - Inheritance

# ----------- Multilevel Inheritance   

class GDad():  # base class
  gdf_name="Apple"
  gdf_type="Big Fruit"

class Dad(GDad): # child class, which inherits GDad class
  f_name="Pear"
  f_type="Medium Fruit"
  
class Son(Dad): # child class, which inherits GDad and Dad class
  s_name="Plum"
  s_type="Small Fruit"

# Accessing GDad class
print("Grand dad name is", GDad.gdf_name, "and type is", GDad.gdf_type)

# Output
# Grand dad name is Apple and type is Big Fruit

# Accessing Dad class
print("Dad name is", Dad.f_name, "and type is", Dad.f_type)

# Output
# Dad name is Pear and type is Medium Fruit

# Accessing GDad/Dad/Son classes through inheritance
# To access GDad/Dad/Son class create object using Son class

obj=Son()
print("Grand dad name is", obj.gdf_name, "and type is", obj.gdf_type)
print("Dad name is", obj.f_name, "and type is", obj.f_type)
print("Son name is", obj.s_name, "and type is", obj.s_type)

# Output
# Grand dad name is Apple and type is Big Fruit
# Dad name is Pear and type is Medium Fruit
# Son name is Plum and type is Small Fruit

# ----------- Multiple Inheritance   

class Dad():  # base class
  f_name="Apple"
  f_type="Big Fruit"

class Mum(): # base class
  m_name="Peach"
  m_type="Bear Fruit"
  
class Son(Dad, Mum): # child class, which inherits Dad and Mum class
  s_name="Plum"
  s_type="Small Fruit"

# Accessing Dad class
print("Dad name is", Dad.f_name, "and type is", Dad.f_type)

# Output
# Dad name is Apple and type is Big Fruit


# Accessing Dad class
print("Mum name is", Mum.m_name, "and type is", Mum.m_type)

# Output
# Mum name is Peach and type is Bear Fruit


# Accessing Dad/Dad/Son classes through inheritance
# To access Dad/Dad/Son class create object using Son class

obj=Son()
print("Dad name is", obj.f_name, "and type is", obj.f_type)
print("Mum name is", obj.m_name, "and type is", obj.m_type)
print("Son name is", obj.s_name, "and type is", obj.s_type)

# Output
# Dad name is Apple and type is Big Fruit
# Mum name is Peach and type is Bear Fruit
# Son name is Plum and type is Small Fruit
