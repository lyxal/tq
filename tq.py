from run import *
from sys import argv

file_loc = argv[1]

prog = open(file_loc,encoding="ascii").read()

# Turn the source code into a list
print(tolist(prog))

list = tolist(prog)

runlist(list)