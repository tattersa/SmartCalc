from src.model.polish_notation import OPERATORS, shunting_yard, calc
from src.view_model.data import logo
from src.view_model.vm_utils import gen_points, numeric, trig_funcs, o_p, convert_to_list
from math import pi


def parse(formula: str):
	number = ''
	trig = ''
	for _ in formula:
		if _ in numeric:  # check if number or dot for float
			number += _
		elif number:  # yield generated number from string on it's end
			yield float(number)
			number = ''  # number is empty again
		elif _ in trig_funcs:
			trig += _
		elif trig:  # yield trigonometry function
			yield trig
			trig = ''
		if _ in OPERATORS or _ in "()":  # if symbol is operator or parenthesis just yield it
			yield _
	if number:  # yielding number on end of string if it exists
		yield float(number)


def prim_pars(formula: str):
	# checking for bad symbols and replace unary + and -
	l_f = convert_to_list(formula)
	new_formula = ''
	for _ in range(len(l_f)):
		if l_f[_] in numeric:
			try:  # check for parenthesis after number
				if _ < len(l_f) - 1 and l_f[_+1] not in numeric \
						and l_f[_+1] == '(' and l_f[_+1] not in o_p:
					return False
			except IndexError:
				return False
		elif l_f[_] in trig_funcs:
			try:  # check for parenthesis in trigonometry function
				if l_f[_+1] not in trig_funcs and l_f[_+1] != '(':
					return False
			except IndexError:
				return False
		elif l_f[_] in o_p or l_f[_] in '()':
			if l_f[_] in '~#':  # check for ~# operators to prevent unexpected behaviour
				return False
			if (_ == 0 and l_f[_] == '-')\
				or (l_f[_] == '-' and l_f[_-1] in o_p):
				l_f[_] = '~'
			elif (_ == 0 and l_f[_] == '+')\
				or (l_f[_] == '+' and l_f[_-1] in o_p):
				l_f[_] = '#'
		else:
			return False
		new_formula += l_f[_]
	# checking for () and it's places
	if new_formula.find('(') != new_formula.find(')') and \
		new_formula.rfind('(') > new_formula.rfind(')'):
		return False
	return new_formula


def x_func(formula: str):

	c_x = gen_points()
	if formula.find('asin') >= 0 or formula.find('acos') >= 0:
		for _ in range(len(c_x)):
			c_x[_] = c_x[_] / 10
	c_y = []
	for _ in range(137):
		x_formula = formula.replace('x', str(c_x[_]))
		x_formula = prim_pars(x_formula)
		if x_formula:
			c_y.append(calc(shunting_yard(parse(x_formula))))
		else:
			return None, None
	return c_x, c_y


def check_parse(formula: str):

	formula = formula.replace('pi', str(pi))
	if formula.find('l33t') >= 0:
		return logo
	elif formula.find('x') >= 0:
		return x_func(formula.replace(' ', ''))
	formula = prim_pars(formula.replace(' ', ''))
	if formula:
		return str(calc(shunting_yard(parse(formula))))
	else:
		return 'Check your formula!'
