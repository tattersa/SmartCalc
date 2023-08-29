import tkinter as tk
import matplotlib.pyplot as pl
import src.view_model.data as data
import src.view_model.vm_utils as vm_ut
from src.view_model.check_parse import check_parse, x_func


pl.rcParams['figure.figsize'] = [7.30, 3.70]
pl.rcParams['figure.autolayout'] = True


root = tk.Tk()
root.geometry('1337x1337')


def temp_text(e, ent):
	ent.delete(0, 'end')


def hist():
	try:
		if data.hi_list[data.curr_h]:
			ent13.delete(0, tk.END)
			ent13.insert(0, data.hi_list[data.curr_h])
		data.curr_h += 1
	except IndexError:
		pass


def graph(c_x: list, c_y: list):
	fig, ax = pl.subplots()
	ax.spines['left'].set_position('center')
	ax.spines['bottom'].set_position('center')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')
	ax.grid('on')
	pl.plot(c_x, c_y, 'b')
	pl.show()


def calc_to_ui(event):
	vm_ut.save_history(str(ent13.get()))
	vm_ut.load_history()
	exp = '1*' + ent13.get()
	x_val = ent37.get()
	if len(x_val) > 0:
		exp = exp.replace('x', ent37.get())
	if exp.find('x') >= 0:
		c_x, c_y = x_func(exp.replace(' ', ''))
		graph(c_x, c_y)
	else:
		res = check_parse(exp)
		ent13.delete(0, tk.END)
		ent13.insert(0, res)


root.bind('<Return>', calc_to_ui)

#  interface
ent13 = tk.Entry(font='Px\\ IBM\\ EGA8 37')
ent37 = tk.Entry(font='Px\\ IBM\\ EGA8 37', justify='center')


ent13.pack(ipady=37)
ent37.pack(ipady=37,)

ent37.insert(0, 'x')
ent37.bind('<FocusIn>', temp_text)

ent13.place(width=1337, height=137, x=137)
ent37.place(width=137, height=137)


root.mainloop()
