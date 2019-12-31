def tolist(n):
	out = []
	str_cnt = 0
	require = 0
	for x,i in enumerate(n):
		if str_cnt%2:
			out.append(out.pop()+i)
			continue

		if i in "0123456789": # Number parser
			if x==0 or n[x-1] not in "0123456789":
				# If previous isn't a number:
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

		while require:
			a,b=out.pop(),out.pop()
			out.append(b+a)

			# Count the quotes in the resulting string
			quote_num = 0
			for i in out[-1]:
				if i == '"' or i == "'":
					quote_num+=1

			print(out)

			if quote_num%2==0:
				out.append(out.pop()+")")
			else:
				out.append(out.pop())

			require -= 1


	# Add the missing quotes back

	lbk = 0
	rbk = 0
	for i in out[-1]:
		if i == '(':
			lbk+=1
		elif i == ')':
			rbk+=1

	out[-1]+=")"*(lbk-rbk)

	return out

def quote(i):
		# Basically an un-eval
		return str([i])[1:-1]

def runlist(out):
	def index(i):
		# For the convenience of non-programmers,
		# The array is 1-indexed.
		return eval(out[i-1])

	for i in out:
		print(eval(i),end="")