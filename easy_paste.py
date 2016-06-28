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

btn_file = tkinter.Button(text='Import Analysis')
var_file = tkinter.StringVar(tk_F)
btn_file.grid(columnspan=2, pady=5)

ent_file = tkinter.Entry(width=35, textvariable=var_file)
ent_file.grid(columnspan=2, pady=5)

lable_rep100 = tkinter.Label(text='Rep and 100%')
lable_rep100.grid(sticky='w', padx=10)

rep100s = [('Joined', 'joined'), ('Separate', 'separate')]
var_rep100 = tkinter.StringVar()
var_rep100.set('joined')
rbs_rep100 = []
for label, rep100 in rep100s:
    rb_rep100 = tkinter.Radiobutton(text=label, variable=var_rep100, value=rep100)
    rb_rep100.grid(row=3, column=rep100s.index((label, rep100)))
    rbs_rep100.append(rb_rep100)

lable_heading = tkinter.Label(text='Headings')
lable_heading.grid(sticky='w', padx=10)

headings = [('New', 'short'), ('Translation -  New', 'long')]
var_heading = tkinter.StringVar()
var_heading.set('short')
rbs_heading = []
for label, heading in headings:
    rb_heading = tkinter.Radiobutton(text=label, variable=var_heading, value=heading)
    rb_heading.grid(row=5, column=headings.index((label, heading)))
    rbs_heading.append(rb_heading)

btn_quote = tkinter.Button(text='Generate table for quote', state='disabled')
btn_quote.grid(columnspan=2, pady=5)

btn_weighted = tkinter.Button(text='Calculate weighted words', state='disabled')
btn_weighted.grid(columnspan=2, pady=5)

btn_folder = tkinter.Button(text='Open folder', state='disabled')
btn_folder.grid(columnspan=2, pady=5)


def import_file(self):
    f_file = tkinter.filedialog.askopenfilename(**args_file)
    if f_file:
        var_file.set(f_file)

btn_file.bind('<ButtonRelease-1>', import_file)


def run_quote(self):
    if btn_quote['state'] == 'normal' or 'active':
        ep_scripts.calc_quote(
            var_file.get(), var_rep100.get(), var_heading.get())

btn_quote.bind('<ButtonRelease-1>', run_quote)


def run_weighted(self):
    if btn_quote['state'] == 'normal' or 'active':
        ep_scripts.calc_weighted(var_file.get())

btn_weighted.bind('<ButtonRelease-1>', run_weighted)


def run_folder(self):
    if btn_folder['state'] == 'normal' or 'active':
        ep_scripts.open_folder(var_file.get())

btn_folder.bind('<ButtonRelease-1>', run_folder)


def select_and_focus(self):
    self.widget.select()
    self.widget.focus()

for rb in rbs_rep100:
    rb.bind('<ButtonRelease-1>', select_and_focus)

for rb in rbs_heading:
    rb.bind('<ButtonRelease-1>', select_and_focus)


def true_false(var, unknown, w):
    if var_file.get():
        btn_quote['state'] = 'normal'
        btn_weighted['state'] = 'normal'
        btn_folder['state'] = 'normal'
    else:
        btn_quote['state'] = 'disabled'
        btn_weighted['state'] = 'disabled'
        btn_folder['state'] = 'disabled'

var_file.trace('w', true_false)


def return_to_click(self):
    tk_F.focus_get().event_generate('<ButtonRelease-1>')

root.bind('<Return>', return_to_click)

top = tk_F.winfo_toplevel()
top.resizable(False, False)
tk_F.mainloop()
