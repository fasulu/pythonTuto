
# ************  How to import and use Modules Package 

'''     INFORMATION

import platform 

this import will import all function related to platform() package

to use it platform.processor()

instead of import platform

if we do as follow;

from platform import *

now we can use platform()'s as processor()

processor()     gives system processor details

In this case we import as * , which will import all function which
we don't need. This way will reduce the performance due overload on memory
So do the following to import function that we need

from platform import system, processor, os, architecture, machine
we can use as

system()        output is Windows
machine()       output is AMD64
architecture()  output is ('64bit', 'WindowsPE')

the above will reduce memomry consumption and increase performace of the programme

'''
