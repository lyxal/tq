from sys import argv

file_loc = argv[1]

prog = open(file_loc,encoding="ascii").read()

run = open("run.py").read()

exec(run)