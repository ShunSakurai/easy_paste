'''
cd dropbox/codes/easy_paste
py -B easy_paste.py
'''
import ep_scripts
import tkinter
import tkinter.filedialog

print('Loading...')

tk_F = tkinter.Frame()

args_file = {'filetypes' : [('csv', '*.csv')]}
# args_file = {'filetypes' : [('csv or html', '*.csv:*.html')]}

btn_file = tkinter.Button(text='Import Analysis')
var_file = tkinter.StringVar(tk_F)
btn_file.grid(columnspan=2, pady=5)

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
    rb_unit.grid(row=3, column=units.index((label, unit)))
    rbs_unit.append(rb_unit)

lable_template = tkinter.Label(text='Templates')
lable_template.grid()

templates = [('New', 'short'), ('Translation -  New', 'long')]
var_template = tkinter.StringVar()
var_template.set('short')
rbs_template = []
for label, template in templates:
    rb_template = tkinter.Radiobutton(text=label, variable=var_template, value=template)
    rb_template.grid(row=5, column=templates.index((label, template)))
    rbs_template.append(rb_template)

btn_generate = tkinter.Button(text='Generate table', state='disabled')
btn_generate.grid(columnspan=2, pady=5)


def import_file(self):
    f_file = tkinter.filedialog.askopenfilename(**args_file)
    var_file.set(f_file)

btn_file.bind('<ButtonRelease-1>', import_file)


def run(self):
    if btn_generate['state'] == 'normal' or 'active':
        ep_scripts.calc_sum(var_file, var_unit, var_template)

btn_generate.bind('<ButtonRelease-1>', run)


def true_false(var, unknown, w):
    if var_file.get():
        btn_generate['state'] = 'normal'
        btn_generate['text'] = 'Generate table!'
    else:
        btn_generate['state'] = 'disabled'
        btn_generate['text'] = 'Generate table'

var_file.trace('w', true_false)

top = tk_F.winfo_toplevel()
top.resizable(False, False)
tk_F.mainloop()
