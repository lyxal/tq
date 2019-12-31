from sys import argv

file_loc = argv[1]

prog = open(file_loc,encoding="ascii").read()

read = [1]

# Turn the source code into a list

out = []
str_cnt = 0
require = 0
input_counter = 0

for x,i in enumerate(prog):
	if str_cnt%2:
		if i == '"' or i == "'":
			str_cnt += 1
		out.append(out.pop()+i)
		continue

	if i in "0123456789": # Number parser
		if x==0 or prog[x-1] not in "+-*/%0123456789":
			# If previous isn't a number:
			# AND isn't an infix operation
			out.append(i)
		else:
			out.append(out.pop()+i)

	elif i == '"' or i == "'": # String parser
		str_cnt += 1
		if str_cnt%2:
			out.append('"'if i=='"'else "'")

	elif i in ".qe":
		if i == '.': # Array indexer
			out.append("index(")
		elif i == 'q': # String quoter
			out.append("quote(")
		elif i == 'e': # eval
			out.append("eval(")
		require+=1

		continue

	elif i in "+-*/%": # Infix addition
		out.append(out.pop()+i)
		require += 1
		continue

	elif i == "p":
		# The previuous item of the current item.
		out.append("prev("+str(len(out))+")")

	elif i == "s":
		# The succeeding item of the current item.
		out.append("succ("+str(len(out))+")")

	elif i == 't': # Tail
		out.append("tail()")

	elif i == 'h': # Head
		out.append("head()")

	elif i == '?': # Get the next input
		out.append("take_i()")

	while require:
		if len(out)>1:
			a,b=out.pop(),out.pop()
			out.append(b+a)

			# Count the quotes in the resulting string
			quote_num = 0
			for i in out[-1]:
				if i == '"' or i == "'":
					quote_num+=1

			if quote_num%2==0:
				out.append(out.pop()+")")
			else:
				out.append(out.pop())

			require -= 1
		else:
			break

# Add the missing quotes back

lbk = 0
rbk = 0

for i in out[-1]:
	if i == '(':
		lbk+=1
	elif i == ')':
		rbk+=1

if lbk>=rbk:
	out[-1]+=")"*(lbk-rbk)
else:
	# Consider removing the abundant brackets
	out[-1]=out[-1][:lbk-rbk]

print(out)

def quote(i):
	# Basically an un-eval
	return str([i])[1:-1]

def index(i):
	# For the convenience of non-programmers,
	# The array is 1-indexed.
	return eval(out[i-1])

def tail():
	# Return the last item of the list
	return eval(out[-1])

def head():
	# Return the first item of the list
	return eval(out[0])

def prev(i):
	# The previous item of the current item
	return eval(out[i-1])

def succ(i):
	# The next item of the current item
	return eval(out[i+1])

def take_i():
	# Take the input based on
	# the current input counter
	return read[input_counter%len(read)]

for x,i in enumerate(out):
	print(eval(i),end="")