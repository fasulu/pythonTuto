# ******--Exception handling by try

try:
  print(x)
except:
  print("Error to process x")
finally:
  x = 2 + 3
  print("Doing finally ",x)


# ******--Exception handling by assert

def age(value):
  assert value > 0 and value < 120, "Please enter valid age"
  print("You entered", value)

getInput=int(input("Please enter your age "))
age(getInput)


# ******--Exception catching

import sys
a= [1,2,3,'q',4,0]
err = []
for i in a:
  try:
    c= 2/i
    print("Result is", c)
    print(abc)                              # This will catch by error
  except:
    print("Error Name", sys.exc_info()[0])   # Prints only error type
    print("Error Detail", sys.exc_info()[1])  # Prints only error detail


# ******--Exception Userdefined

class Error(Exception):
  pass
class SmallNumErr(Error):
  pass
class LargerNumErr(Error):
  pass
class NotNumber(Error):
  pass

num=10
print("Number guessing game")
while True:
  try:
    choice=int(input("Please enter a number "))
    if int(choice)<10:
      raise SmallNumErr
    elif int(choice)>10:
      raise LargerNumErr
    break
  except SmallNumErr:
    print("Entered small number, increase your number")
  except LargerNumErr:
    print("Entered large number, decrease your number")
  except:
    print("Invalid number")
print("Congratulation, you are correct")
exit()