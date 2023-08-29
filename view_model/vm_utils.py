import src.view_model.data
numeric = '1234567890.'  # all numbers and dot for float
trig_funcs = 'sincoltaqrg'  # all trigonometry functions
o_p = '+-#~(*/^%'  # symbols for correct unary + and - values


def gen_points():
	x = -6.8
	c_x = []
	for _ in range(137):
		c_x.append(x)
		x = round(x + 0.1, 2)
	return c_x


def clear_history():
	open('hist.ory', 'w').close()


def convert_to_list(string: str):
	string_list = []
	string_list[:0] = string
	return string_list


def save_history(exp: str):
	with open('hist.ory', 'a') as hist:
		hist.write(str(exp + '\n'))


def load_history():
	hist = open('hist.ory')
	src.view_model.data.hi_list = hist.readlines()
	src.view_model.data.hi_list.reverse()
	hist.close()
	for _ in range(len(src.view_model.data.hi_list)):
		src.view_model.data.hi_list[_] = src.view_model.data.hi_list[_].replace('\n', '')
	src.view_model.data.curr_h = 0
