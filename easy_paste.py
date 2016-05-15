'''
cd dropbox/codes/easy_paste
py -B easy_paste.py
'''
import ep_scripts
import tkinter
import tkinter.filedialog

print('Loading...')

root = tkinter.Tk()
tk_F = tkinter.Frame(root)

args_file = {'filetypes' : [('csv', '*.csv')]}
# args_file = {'filetypes' : [('csv or html', '*.csv:*.html')]}

btn_file = tkinter.Button(text='Import Analysis')
var_file = tkinter.StringVar(tk_F)
btn_file.grid(columnspan=2, pady=5)

ent_file = tkinter.Entry(width=35, textvariable=var_file)
ent_file.grid(columnspan=2)

lable_unit = tkinter.Label(text='Units')
lable_unit.grid(sticky='w', padx=10)

units = [('Word', 'word'), ('Character\n*Not supported', 'char')]
var_unit = tkinter.StringVar()
var_unit.set('word')
rbs_unit = []
for label, unit in units:
    rb_unit = tkinter.Radiobutton(text=label, variable=var_unit, value=unit)
    rb_unit.grid(row=3, column=units.index((label, unit)))
    rbs_unit.append(rb_unit)

lable_rep100 = tkinter.Label(text='Rep and 100%')
lable_rep100.grid(sticky='w', padx=10)

rep100s = [('Joined', 'joined'), ('Separate', 'separate')]
var_rep100 = tkinter.StringVar()
var_rep100.set('joined')
rbs_rep100 = []
for label, rep100 in rep100s:
    rb_rep100 = tkinter.Radiobutton(text=label, variable=var_rep100, value=rep100)
    rb_rep100.grid(row=5, column=rep100s.index((label, rep100)))
    rbs_rep100.append(rb_rep100)

lable_heading = tkinter.Label(text='Headings')
lable_heading.grid(sticky='w', padx=10)

headings = [('New', 'short'), ('Translation -  New', 'long')]
var_heading = tkinter.StringVar()
var_heading.set('short')
rbs_heading = []
for label, heading in headings:
    rb_heading = tkinter.Radiobutton(text=label, variable=var_heading, value=heading)
    rb_heading.grid(row=7, column=headings.index((label, heading)))
    rbs_heading.append(rb_heading)

btn_generate = tkinter.Button(text='Generate table', state='disabled')
btn_generate.grid(columnspan=2, pady=5)


def import_file(self):
    f_file = tkinter.filedialog.askopenfilename(**args_file)
    var_file.set(f_file)

btn_file.bind('<ButtonRelease-1>', import_file)


def run(self):
    if btn_generate['state'] == 'normal' or 'active':
        ep_scripts.calc_sum(var_file, var_unit, var_rep100, var_heading)

btn_generate.bind('<ButtonRelease-1>', run)


def select_and_focus(self):
    self.widget.select()
    self.widget.focus()

for rb in rbs_unit:
    rb.bind('<ButtonRelease-1>', select_and_focus)

for rb in rbs_rep100:
    rb.bind('<ButtonRelease-1>', select_and_focus)

for rb in rbs_heading:
    rb.bind('<ButtonRelease-1>', select_and_focus)


def true_false(var, unknown, w):
    if var_file.get():
        btn_generate['state'] = 'normal'
        btn_generate['text'] = 'Generate table!'
    else:
        btn_generate['state'] = 'disabled'
        btn_generate['text'] = 'Generate table'

var_file.trace('w', true_false)


def return_to_click(self):
    tk_F.focus_get().event_generate('<ButtonRelease-1>')

root.bind('<Return>', return_to_click)

top = tk_F.winfo_toplevel()
top.resizable(False, False)
tk_F.mainloop()
