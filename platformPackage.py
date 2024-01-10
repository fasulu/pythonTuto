
# ************  platform()

'''   The Platform module is used to retrieve as much possible information 
about the platform(system) on which the program is being currently executed. 
        
'''

import platform
  
import platform 
  
# displaying platform processor 
print('Platform processor:', platform.processor())  # Platform processor: Intel64 Family 6 Model 42 Stepping 7, GenuineIntel
  
# displaying platform architecture 
print('Platform architecture:', platform.architecture()) # Platform architecture: ('64bit', 'WindowsPE')

# displaying machine type 
print('Machine type:', platform.machine())  # Machine type: AMD64

# displaying system network name 
print("System's network name:", platform.node())    # System's network name: DESKTOP-M0R89XH

# displaying platform information 
print('Platform information:', platform.platform())     # Platform information: Windows-10-10.0.19045-SP0

# displaying system info 
print('System info:', platform.system())    # System info: Windows

# displaying python build date and no. 
print('Python build no. and date:', platform.python_build())# Python build no. and date: ('tags/v3.10.4:9d38120', 'Mar 23 2022 23:13:41')

# displaying python compiler 
print('Python compiler:', platform.python_compiler())   # Python compiler: MSC v.1929 64 bit (AMD64)

# displaying python SCM info 
print('Python implementation:', platform.python_implementation())   # Python implementation: CPython
