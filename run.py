read = [1] # Fork Note: I haven't tested to see if this is still needed with my other changes
separ = ""

# Turn the source code into a list

out = []
str_cnt = 0
require = 0
input_counter = 0

lenq = 0


def quote(i):
    # Basically an un-eval
    # Use the built-in.
    return repr(i)

def index(i):
    # For the convenience of non-programmers,
    # The array is 1-indexed.
	
    # Fork Note: This is also for the annoyance of non-non-programmers
    return eval(out[i - 1])


def tail():
    # Return the last item of the list
    return eval(out[-1])


def head():
    # Return the first item of the list
    return eval(out[0])


def prev(i):
    # The previous item of the current item
    return eval(out[i - 1])


def prev2(i):
    # A special built-in for 2 items before
    # the current item
    return eval(out[i - 2])


def succ(i):
    # The next item of the current item
    return eval(out[i + 1])


def take_i():
    # Take the input based on
    # the current input counter
    return eval(input()) # Fork Note: Uses dynamic input rather than a list. Although I realise input lists might be needed
                         # like I implemented them in Keg.


def extend(i):
    x = out
    while 1:
        x.insert(-1, quote(eval(i)))
        print(eval(x[-2]), end=separ)
        del x[0]
    return x


for x, i in enumerate(prog):
    lenq = len(out) - require
    if str_cnt % 2:
        if i == '"' or i == "'":
            str_cnt += 1
        out.append(out.pop() + i)
        continue

    if i in "0123456789":  # Number parser
        if x == 0 or prog[x - 1] not in "+-*/%0123456789":
            # If previous isn't a number:
            # AND isn't an infix operation
            out.append(i)
        else:
            if prog[x - 1] == "0":
                # Leading zeros in decimals
                # aren't permitted
                out.append(i)
            else:
                out.append(out.pop() + i)

    elif i == '"' or i == "'":  # String parser
        str_cnt += 1
        if str_cnt % 2:
            out.append('"' if i == '"' else "'")

    elif i in ".qe":
        if i == '.':  # Array indexer
            out.append("index(")
        elif i == 'q':  # String quoter
            out.append("quote(")
        elif i == 'e':  # eval
            out.append("eval(")
        require += 1

        continue

    elif i in "+-*/%":  # Infix addition
        if prog[x - 1] not in 'prsthi?0123456789"\'':
            # i.e. not a constant
            # it's gonna be a monad
            out.append(i)
            require -= 1
            # Monads don't need requires
            # I don't know why
        else:
            out.append(out.pop() + i)
        require += 1
        continue

    elif i == "p":
        # The previous item of the current item.
        out.append("prev(" + str(lenq) + ")")

    elif i == "r":
        # 2 items before the current item.
        out.append("prev2(" + str(lenq) + ")")

    elif i == "s":
        # The succeeding item of the current item.
        out.append("succ(" + str(len(out)) + ")")

    elif i == 't':  # Tail
        out.append("tail()")

    elif i == 'h':  # Head
        out.append("head()")

    elif i == "i":
        # The index of the current item
        out.append(str(len(out) + 1))

    elif i == '?':  # Get the next input
        out.append("take_i()")

    elif i == ')':  # Extend out with the previous item
        a = out.pop()
        out.append("extend(" + quote(a) + ")")

    while require:
        if len(out) > 1:
            a, b = out.pop(), out.pop()
            out.append(b + a)

            # Count the quotes in the resulting string
            quote_num = 0
            for i in out[-1]:
                if i == '"' or i == "'":
                    quote_num += 1

            if quote_num % 2 == 0:
                pass
            else:
                out.append(out.pop())

            require -= 1
        else:
            break

# Add the missing quotes back

for x, i in enumerate(out):
    for j in i:
        lbk = 0
        rbk = 0
        if j == '(':
            lbk += 1
        elif j == ')':
            rbk += 1
        if lbk >= rbk:
            out[x] += ")" * (lbk - rbk)
        else:
            # Consider removing the abundant brackets
            out[x] = out[x][:lbk - rbk]

for x, i in enumerate(out):
    expression = eval(i)

'''

Extended Fork Note:

Having `eval(i)` twice isn't a good idea.
Why? Because first of all, that's resources being wasted
when the result could be stored in a variable.
Secondly, when using dynamic input lists, it would ask
for input more than once.


'''
    if expression == "":
        continue
    else:
        print(expression, end=separ)
