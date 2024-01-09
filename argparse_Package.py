# ******--    argparse package

# ----------- 

import argparse

parser = argparse.ArgumentParser()                
parser.add_argument('str', help='enter a string')
args=parser.parse_args()
print(args.str)


# When we start he programme as python temp.py -h

# output

# usage: temp.py [-h] str
# positional arguments:
#   str         enter a string
# options:
#   -h, --help  show this help message and exit


# ----------- With identifier

import argparse

parser = argparse.ArgumentParser()                
parser.add_argument('-name', '--Student_name', required=True, help='enter student name')
parser.add_argument('-age', '--Student_age', required=True, help='enter student age')

args=parser.parse_args()
print(args)


# When we start the programme as <python temp.py -name metayaer -age 5>

# output

# Namespace(Student_name='metayaer', Student_age='5')
