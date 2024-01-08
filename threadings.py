# ******--Threads - To run several functions run simultaneously

# ----------- Without threading

def do_A():
  count=0
  while count<3:
    count+=1
    print("function do_A",count)

def do_B():
  count=0
  while count<3:
    count+=1
    print("function do_B",count)

do_A()
do_B()
# Will finish function <do_A> then start function <do_B>, 
# this functions are not running through threading method

# Output
# function do_A 1
# function do_A 2
# function do_A 3
# function do_B 1
# function do_B 2
# function do_B 3

# ----------- With threading

# to use thread we need import 2 python libraries.
import _thread
import time

def do_C(msg):
  count=0
  while count<3:
    count+=1
    time.sleep(1)
    print(msg)

def do_D(msg):
  count=0
  while count<3:
    count+=1
    time.sleep(3)
    print(msg)

try:
  _thread.start_new_thread(do_C,("function do_C",))
  _thread.start_new_thread(do_D,("function do_D",))

except (KeyboardInterrupt, SystemExit):
  print("Error occured")
    
while 1:    # to start threading function
  pass  

# ----------- Thread using threading library

import threading
import time
from datetime import datetime

def display():
  for i in range(5):
    time.sleep(2)

    timenow = time.localtime()                        # using time
    current_time = time.strftime("%H:%M:%S", timenow) # using time
    print("Time is", current_time)                    # using time

    # timenow=datetime.now()                          # using datetime
    # current_time=timenow.strftime("%H:%M:%S")       # using datetime
    # print("Time is", current_time)                  # using datetime

thd=threading.Thread(target=display)
thd.start()

# ----------- Passing 2 arguments for threading

import threading
import time
from datetime import datetime

def display(times, sleep_time):
  for i in range(times):
    time.sleep(sleep_time)

    timenow = time.localtime()                        # using time
    current_time = time.strftime("%H:%M:%S", timenow) # using time
    print("Time is", current_time)                    # using time

    # timenow=datetime.now()                          # using datetime
    # current_time=timenow.strftime("%H:%M:%S")       # using datetime
    # print("Time is", current_time)                  # using datetime

thd=threading.Thread(target=display, args=(5,2,))     # pass arguments for threading
thd.start()

# ----------- Passing arguments and parameters for threading

import threading
import time
from datetime import datetime

def display_A(times, sleep_time, thread_name):
  for i in range(times):
    time.sleep(sleep_time)

    timenow = time.localtime()                        # using time
    current_time = time.strftime("%H:%M:%S", timenow) # using time
    print(thread_name, "time is", current_time)                    # using time

    # timenow=datetime.now()                          # using datetime
    # current_time=timenow.strftime("%H:%M:%S")       # using datetime
    # print("Time is", current_time)                  # using datetime

def display_B(times, sleep_time, thread_name):
  for i in range(times):
    time.sleep(sleep_time)

    timenow = time.localtime()                        # using time
    current_time = time.strftime("%H:%M:%S", timenow) # using time
    print(thread_name, "time is", current_time)                    # using time

    # timenow=datetime.now()                          # using datetime
    # current_time=timenow.strftime("%H:%M:%S")       # using datetime
    # print("Time is", current_time)                  # using datetime

thd1=threading.Thread(target=display_A, args=(5,1,"Thread-1"))     # pass arguments for threading
thd1.start()
thd2=threading.Thread(target=display_B, args=(5,2,"Thread-2"))     # pass arguments for threading
thd2.start()

# ----------- Identifying thread name using setName() and getName()

import threading
import time

def display_A(times):
  for i in range(5):
    time.sleep(times+1.2)
    
    timenow = time.localtime()                        # using time
    current_time = time.strftime("%H:%M:%S", timenow) # using time

    current_thd=threading.current_thread().getName()  # get the name of the current thread

    print("Current thread name is ", current_thd, "started at", current_time) # using time

for p in range(5):
  thd1=threading.Thread(target=display_A, args=(p,))
  thd1.setName(str(p))                                # set a name for the thread    
  thd1.start()


# ----------- Check thread is alive or not

import threading
import time

def display_A(times):
  
  time.sleep(times)
  return

thd1=threading.Thread(target=display_A, args=(4,), name= "Thread1")
thd1.start()
thd2=threading.Thread(target=display_A, args=(2,), name= "Thread2")
thd2.start()

for p in range(5):
  time.sleep(p+0.2)
  print("[",time.ctime(),thd1.name,thd1.is_alive(),"]")
  print("[",time.ctime(),thd2.name,thd2.is_alive(),"]")


# ----------- Daemon threads

import threading
import time

def doctorA():  
  print("Time", time.ctime(), "thread 1 started")
  time.sleep(10)
  print("Time", time.ctime(), "thread 1 finished")

def doctorB():  
  print("Time", time.ctime(), "thread 2 started")
  print("Time", time.ctime(), "thread 2 finished")

thd1=threading.Thread(target=doctorA, daemon="true")  # daemon thread will run untill programme end
thd2=threading.Thread(target=doctorB,)
thd1.start()
thd2.start()
thd1.join()   # will show finished or not
thd2.join()   # will show finished or not


# -----------Using builtin Timer from threading package instead of time.sleep()

import threading

def demo():
  print("Using Timer instead of time.sleep() appears after 3 seconds")

thd=threading.Timer(3.0, demo)
thd.start()

# Output
# Using Timer instead of time.sleep() appears after 3 seconds


# ******--Sub class thread

# ----------- A simple subclass thread

import threading

class ThreadDemo(threading.Thread):
  def run(self):                      # run() is the method available in threading.Tread
    print("Hello")
    self.new()
    return

  def new(self):
    print("Welcome")

for i in range(3):      # programme starts from here
  thd=ThreadDemo()      # assigned ThreadDemo
  thd.start()           # ThreadDemo starts and call run(self) then new(self)

# Output

# Hello
# Welcome
# Hello
# Welcome
# Hello
# Welcome


# -----------Passing arguments with subclass

import threading

class ThreadDemo(threading.Thread):
  def __init__(self, args=(), kwargs = None):   # create constructor
    threading.Thread.__init__(self)
    self.args=args
    self.kwargs=kwargs  
  
  def run(self):                      # run() is a method available in threading.Tread
    print("thread", self.args, "argument is",self.kwargs)
    return

for i in range(3):                                # programme starts from here
  thd=ThreadDemo(args=(i,), kwargs="Hello")       # assigned ThreadDemo
  thd.start()                                     # ThreadDemo starts and call run(self) then new(self)

# Output

# thread (0,) argument is Hello
# thread (1,) argument is Hello
# thread (2,) argument is Hello


# ----------- current_thread(), enumerate(), active_count()

import threading
import time

def worker_A():
  print("Thread started")
  print(threading.current_thread())     # gives current running thread's id
  time.sleep(5)

for x in range(3):
  thd=threading.Thread(target=worker_A)
  thd.start()
  time.sleep(2)

print("Thread enumerate")
print(threading.enumerate())      # gives how many threads running in a list
print("Thread total count")
print(threading.active_count())     # gives total active thread count
# Output

# Thread started
# <Thread(Thread-1, started 140628015617792)>
# Thread started
# <Thread(Thread-2, started 140628007225088)>
# Thread started
# <Thread(Thread-3, started 140627998832384)>

# Thread enumerate
# [
  # <_MainThread(MainThread, started 139839505688384)>, 
  # <Thread(Thread-2, started 139839489251072)>, 
  # <Thread(Thread-3, started 139839480858368)>
# ]
# Thread total count
# 3

# -----------Event in thread


import threading
import time

def isSet():
  time.sleep(2)
  event.set()                       # after 2 seconds event set to True
  print("Event is set(true)")
  time.sleep(5)                     # waits for 5 seconds
  event.clear()                     # after 5 seconds event set to False
  print("Event is cleared(false)")

def eventOperation():
  event.wait()
  while event.is_set():             # check is the event is False, if true says waiting for signal
    time.sleep(1)
    print("thread is waiting(",time.ctime(), ") for signal")
  print("thread received signal")   # if signal received prints

event=threading.Event()             # threading event created
thd1=threading.Thread(target=isSet)           # isSet() assignted 
thd2=threading.Thread(target=eventOperation)  # eventOperation() assignted 
thd1.start()    # thread function started
thd2.start()    # thread function started
thd1.join()
thd2.join()

# Output

# Event is set(true)
# thread is waiting( Fri Jan  5 16:10:56 2024 ) for signal
# thread is waiting( Fri Jan  5 16:10:57 2024 ) for signal
# thread is waiting( Fri Jan  5 16:10:58 2024 ) for signal
# thread is waiting( Fri Jan  5 16:10:59 2024 ) for signal
# Event is cleared(false)
# thread is waiting( Fri Jan  5 16:11:00 2024 ) for signal
# thread received signal

# ----------- acquire() and release() in thread
              # acquire() will lock the thread untill it finish its work
              # release() will release the lock once job finished

import threading
import time

lock=threading.Lock()

def startThread(name):
  time.sleep(1)
  lock.acquire()
  display(name)
  lock.release()

def display(name):
  for x in range(5):
    time.sleep(2)
    print(name, "Executed:", x)

thd1=threading.Thread(target=startThread, args=("Thread:1",))           # isSet() assignted 
thd2=threading.Thread(target=startThread, args=("Thread:2",))  # eventOperation() assignted 
thd3=threading.Thread(target=startThread, args=("Thread:3",))  # eventOperation() assignted 
thd1.start()    # thread function started
thd2.start()    # thread function started
thd3.start()    # thread function started
thd1.join()
thd2.join()
thd3.join()

# Output

  # Result without after lock() and acquire()
# Thread:1 Executed: 0
# Thread:2 Executed: 0
# Thread:3 Executed: 0
# Thread:1 Executed: 1
# Thread:2 Executed: 1
# Thread:3 Executed: 1
# Thread:1 Executed: 2
# Thread:2 Executed: 2
# Thread:3 Executed: 2
# Thread:1 Executed: 3
# Thread:2 Executed: 3
# Thread:3 Executed: 3
# Thread:1 Executed: 4
# Thread:2 Executed: 4
# Thread:3 Executed: 4

  # Result after lock() and acquire()
# Thread:2 Executed: 0
# Thread:2 Executed: 1
# Thread:2 Executed: 2
# Thread:2 Executed: 3
# Thread:2 Executed: 4
# Thread:1 Executed: 0
# Thread:1 Executed: 1
# Thread:1 Executed: 2
# Thread:1 Executed: 3
# Thread:1 Executed: 4
# Thread:3 Executed: 0
# Thread:3 Executed: 1
# Thread:3 Executed: 2
# Thread:3 Executed: 3
# Thread:3 Executed: 4


# ----------- acquire() and release() in thread
              # acquire() will lock the thread untill it finish its work
              # release() will release the lock once job finished

import threading as thd

class Thread:
  def __inti__(self):
    self.a=5
    self.b=10
    self.lock=thd.RLock()

  def first(self):
    print("Entering into first function")
    with self.lock:
      self.a +=5

  def second(self):
    print("Entering into second function")
    with self.lock:
      self.b -=5

  def main(self):
    print("Entering into main function")
    with self.lock:
      self.first()
      self.second()
      print(self.a, self.b)

obj=Thread()
obj.main()

# Output
  # ***************Following error Need to fix*****************
# Entering into main function
# Traceback (most recent call last):
#   File "/home/fasulu/PycharmProjects/temp.py", line 35, in <module>
#     obj.main()
#   File "/home/fasulu/PycharmProjects/temp.py", line 29, in main
#     with self.lock:
# AttributeError: 'Thread' object has no attribute 'lock'
