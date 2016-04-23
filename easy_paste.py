'''
cd dropbox/codes/easy_paste
py -B easy_paste.py
'''

import ep_scripts
import tkinter
import tkinter.filedialog

tk_F = tkinter.Frame()

args_file = {'filetypes' : [('csv', '*.csv')]}
# args_file = {'filetypes' : [('csv or html', '*.csv:*.html')]}

btn_file = tkinter.Button(text='Import Analysis')
var_file = tkinter.StringVar(tk_F)
btn_file.grid(columnspan=2, pady=5)


def import_file(self):
    f_file = tkinter.filedialog.askopenfilename(**args_file)
    var_file.set(f_file)

btn_file.bind('<ButtonRelease-1>', import_file)

ent_file = tkinter.Entry(width=35, textvariable=var_file)
ent_file.grid(columnspan=2)

lable_unit = tkinter.Label(text='Units')
lable_unit.grid()

units = [('Word', 'word'), ('Character*\n*HTML only and\nnot supported', 'char')]
var_unit = tkinter.StringVar()
var_unit.set('word')
rbs_unit = []
for label, unit in units:
    rb_unit = tkinter.Radiobutton(text=label, variable=var_unit, value=unit)
    rb_unit.grid(row=2, column=units.index((label, unit)))
    rbs_unit.append(rb_unit)


def run(self):
    if btn_run['state'] == 'normal' or 'active':
        ep_scripts.calc_sum(var_file, var_unit)

btn_run = tkinter.Button(text='Run', state='disabled')
btn_run.grid(columnspan=2, pady=5)
btn_run.bind('<ButtonRelease-1>', run)


def true_false(var, unknown, w):
    if var_file.get():
        btn_run['state'] = 'normal'
        btn_run['text'] = 'Run!'
    else:
        btn_run['state'] = 'disabled'
        btn_run['text'] = 'Run'

var_file.trace('w', true_false)

top = tk_F.winfo_toplevel()
top.resizable(False, False)
tk_F.mainloop()
