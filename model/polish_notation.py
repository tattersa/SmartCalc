from math import sin, cos, tan, acos, \
		asin, atan, sqrt, log

# dictionary of operators, it's priority and lambda funcs for operations
OPERATORS = {
	'+': (1, lambda x, y: x + y),
	'-': (1, lambda x, y: x - y),
	'*': (2, lambda x, y: x * y),
	'/': (2, lambda x, y: x / y),
	'%': (2, lambda x, y: x % y),
	'^': (3, lambda x, y: x ** y),
	'#': (4, lambda x: +x),
	'~': (4, lambda x: -x),
	'sin': (4, lambda x: sin(x)),
	'cos': (4, lambda x: cos(x)),
	'tan': (4, lambda x: tan(x)),
	'acos': (4, lambda x: acos(x)),
	'asin': (4, lambda x: asin(x)),
	'atan': (4, lambda x: atan(x)),
	'sqrt': (4, lambda x: sqrt(x)),
	'ln': (4, lambda x: log(x)),
	'log': (4, lambda x: log(x, 10))
}


def shunting_yard(parsed_formula):
	stack = []  # list in python is also stack
	for token in parsed_formula:
		# all operators are right-associated. Sorting it by polish notation priority rules
		if token in OPERATORS:
			while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
				yield stack.pop()
			stack.append(token)
		elif token == ")":
			# if meet closing parenthesis getting all elements from stack to opening parenthesis
			# and removing it (opening parenthesis) from stack
			while stack:
				x = stack.pop()
				if x == "(":
					break
				yield x
		elif token == "(":
			stack.append(token)  # just place opening parenthesis in stack
		else:
			yield token  # yield token if token is number
	while stack:
		yield stack.pop()


def calc(polish):
	stack = []
	try:
		for token in polish:
			if token in OPERATORS:  # if element is operator:
				if OPERATORS[token][0] == 4 and stack:  # if token priority is trigonometry function
					x = stack.pop()  # take number from stack
					stack.append(OPERATORS[token][1](x))  # calculating function
				else:
					y, x = stack.pop(), stack.pop()  # taking 2 numbers from stack
					stack.append(OPERATORS[token][1](x, y))  # calculating operator, sending result back to stack
			else:
				stack.append(token)
		return stack[0]  # last remaining number in stack is our result
	except Exception:
		return 'Error! Yor formula is completely wrong!'
		pass
