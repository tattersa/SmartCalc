import tkinter as tk
from src.view_model.check_parse import check_parse, x_func
import src.view_model.data as data
import matplotlib.pyplot as pl
import src.view_model.vm_utils as vm_ut


pl.rcParams['figure.figsize'] = [7.30, 3.70]
pl.rcParams['figure.autolayout'] = True


def calc_to_ui(event):
	vm_ut.save_history(str(ent.get()))
	vm_ut.load_history()
	exp = '1*' + ent.get()
	x_val = ent2.get()
	if len(x_val) > 0:
		exp = exp.replace('x', ent2.get())
	if exp.find('x') >= 0:
		c_x, c_y = x_func(exp.replace(' ', ''))
		graph(c_x, c_y)
	else:
		r = check_parse(exp)
		lab["text"] = r


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


def exit_ui():
	root.destroy()
	exit(1337)


def hist():
	try:
		if data.hi_list[data.curr_h]:
			ent.delete(0, tk.END)
			ent.insert(0, data.hi_list[data.curr_h])
		data.curr_h += 1
	except IndexError:
		pass


root = tk.Tk()
root.title("SmartCalc")
root.geometry("737x737")
root.bind('<Return>', calc_to_ui)
ent = tk.Entry(font='Px\\ IBM\\ EGA8 15', width=137)
but = tk.Button(font='Px\\ IBM\\ EGA8 15', text="Calculate")
lab = tk.Label(root, text=data.help_label, font='Px\\ IBM\\ EGA8 15', justify='left')
butExit = tk.Button(root, text="Exit", command=exit_ui, font='Px\\ IBM\\ EGA8 15')
butt = tk.Button(root, font='Px\\ IBM\\ EGA8 15', text="lexus", command=hist)
butt2 = tk.Button(root, font='Px\\ IBM\\ EGA8 15', text="1337", command=vm_ut.clear_history())
ent2 = tk.Entry(font='Px\\ IBM\\ EGA8 15', width=137)

but.bind('<Button-1>', calc_to_ui)

ent.place(width=137, height=137)
but.place(width=337, height=373)
lab.place(width=737, height=737)
butt.place(width=337, height=373, x=137, y=137)
butt2.place(width=337, height=373, x=228, y=337)
ent2.place(width=137, height=37, y=37)

ent.pack(ipady=3)
but.pack()
butExit.pack()
lab.pack()
butt.place()
ent2.place()

vm_ut.load_history()
root.mainloop()
