'''
cd dropbox/codes/easy_paste
py -B easy_paste.py
'''
import ep_scripts
import setup
import tkinter
import tkinter.filedialog

print('Loading v', setup.dict_console['version'], '...', sep='')

root = tkinter.Tk()
tk_F = tkinter.Frame(root)
str_gray = 'dark slate gray'
str_default_color = 'SystemButtonFace'


class Border(tkinter.Frame):
    def __init__(self):
        super().__init__(height=30)


args_file = {'filetypes' : [('csv', '*.csv')]}

btn_file = tkinter.Button(text='Import Analysis Files')
var_files = tkinter.StringVar()
btn_file.grid(columnspan=2, pady=5)

ent_file = tkinter.Entry(width=55, textvariable=var_files)
ent_file.grid(columnspan=2, pady=5)

row_open = ep_scripts.get_next_grid_row(root)

var_result = tkinter.BooleanVar()
cb_result = tkinter.Checkbutton(text='Open after export', variable=var_result)
cb_result.select()
cb_result.grid(row=row_open, column=0, pady=5)

btn_folder = tkinter.Button(text='Open folder', state='disabled')
btn_folder.grid(row=row_open, column=1, pady=5)

lable_unit = tkinter.Label(text='Unit')
lable_unit.grid(sticky='w', padx=10)

units = [('Word', 'word'), ('Character', 'char')]
var_unit = tkinter.StringVar()
var_unit.set('word')
rbs_unit = []
row_unit = ep_scripts.get_next_grid_row(root)
for label, unit in units:
    rb_unit = tkinter.Radiobutton(text=label, variable=var_unit, value=unit)
    rb_unit.grid(row=row_unit, column=units.index((label, unit)), sticky='w', padx=5)
    rbs_unit.append(rb_unit)

frame_border1 = Border()
frame_border1.grid()

label_mr_categories = tkinter.Label(text=r'Categorize match rates')
label_mr_categories.grid(sticky='w', padx=10)

frame_mr_categories = tkinter.Frame()
frame_mr_categories.grid(columnspan=2, pady=10)
tuple_str_mr = ('New', '50-74%', '75-84%', '85-94%', '95-99%', '100%', 'Reps')

row_mrc_labels = ep_scripts.get_next_grid_row(frame_mr_categories)
list_mrc_labels = []

for str_mr in tuple_str_mr:
    label_mr_category = tkinter.Label(frame_mr_categories, text=str_mr)
    label_mr_category.grid(row=row_mrc_labels, column=tuple_str_mr.index(str_mr) * 2, pady=5)
    list_mrc_labels.append(label_mr_category)

row_mr_categories = ep_scripts.get_next_grid_row(frame_mr_categories)
list_match_rate_labels = []
list_separator_labels = []

for str_mr in tuple_str_mr:
    label_match_rate = tkinter.Label(frame_mr_categories, text=str_mr)
    label_match_rate.grid(row=row_mr_categories, column=tuple_str_mr.index(str_mr) * 2, pady=5)
    list_match_rate_labels.append(label_match_rate)

for i in range(len(list_match_rate_labels) - 1):
    label_separator = tkinter.Label(frame_mr_categories, text=' ')
    label_separator.grid(row=row_mr_categories, column=i * 2 + 1)
    list_separator_labels.append(label_separator)

for i in [1, 4]:
    list_separator_labels[i]['bg'] = str_gray

lable_heading = tkinter.Label(text='Headings')
lable_heading.grid(sticky='w', padx=10)

headings = [('New', 'short'), ('Translation -  New', 'long')]
var_heading = tkinter.StringVar()
var_heading.set('short')
rbs_heading = []
row_heading = ep_scripts.get_next_grid_row(root)
for label, heading in headings:
    rb_heading = tkinter.Radiobutton(text=label, variable=var_heading, value=heading)
    rb_heading.grid(row=row_heading, column=headings.index((label, heading)), sticky='w', padx=5)
    rbs_heading.append(rb_heading)

btn_quote = tkinter.Button(text='Generate table for quote', state='disabled')
btn_quote.grid(columnspan=2, pady=10)

frame_border2 = Border()
frame_border2.grid()

lable_wwt_style = tkinter.Label(text='Weighted styles')
lable_wwt_style.grid(sticky='w', padx=10)

wwt_styles = [
    ('Wds, TrHrs, Pr...', 'time_first'),
    ('Repeated, 100%...', 'words_first')]
var_wwt_style = tkinter.StringVar()
var_wwt_style.set('time_first')
rbs_wwt_style = []
row_style = ep_scripts.get_next_grid_row(root)
for label, wwt_style in wwt_styles:
    rb_wwt_style = tkinter.Radiobutton(text=label, variable=var_wwt_style, value=wwt_style)
    rb_wwt_style.grid(row=row_style, column=wwt_styles.index((label, wwt_style)), sticky='w', padx=5)
    rbs_wwt_style.append(rb_wwt_style)

lable_total = tkinter.Label(text='Calculate totals')
lable_total.grid(sticky='w', padx=10)

row_total = ep_scripts.get_next_grid_row(root)

var_total_col = tkinter.BooleanVar()
cb_total_col = tkinter.Checkbutton(text='Total columns', variable=var_total_col)
cb_total_col.select()
cb_total_col.grid(row=row_total, column=0, sticky='w', padx=5)

var_total_row = tkinter.BooleanVar()
cb_total_row = tkinter.Checkbutton(text='Total row', variable=var_total_row)
cb_total_row.select()
cb_total_row.grid(row=row_total, column=1, sticky='w', padx=5)

btn_weighted = tkinter.Button(text='Calculate weighted words', state='disabled')
btn_weighted.grid(columnspan=2, pady=10)

frame_border3 = Border()
frame_border3.grid()

row_about = ep_scripts.get_next_grid_row(root)

btn_readme = tkinter.Button(text='Read readme', command=ep_scripts.open_readme)
btn_readme.grid(row=row_about, column=0, pady=5)

btn_update = tkinter.Button(text='Check for updates', command=ep_scripts.check_updates)
btn_update.grid(row=row_about, column=1, pady=5)


def import_file(self):
    initial_dir = ep_scripts.dir_from_str_path(ep_scripts.divide_str_tuple(var_files.get())[0])
    f_files = tkinter.filedialog.askopenfilenames(initialdir=initial_dir, **args_file)
    if f_files:
        var_files.set(f_files)


btn_file.bind('<ButtonRelease-1>', import_file)


def toggle_label_color(self):
    if self.widget['bg'] == str_gray:
        self.widget['bg'] = str_default_color
    else:
        self.widget['bg'] = str_gray


def get_separators():
    list_separators = []
    for i in range(len(list_separator_labels)):
        if list_separator_labels[i]['bg'] == str_gray:
            list_separators.append(True)
        else:
            list_separators.append(False)
    return list_separators


def adjust_colspan():
    list_separators = get_separators()
    list_mr_text = ep_scripts.return_mrc_text(list_separators)
    list_colspan = ep_scripts.return_mrc_colspan(list_separators)

    for mrcl in list_mrc_labels:
        mrcl.grid_forget()
    list_mrc_labels.clear()

    next_column = 0
    for mrt, cs in zip(list_mr_text, list_colspan):
        label_mr = tkinter.Label(frame_mr_categories, text=mrt)
        label_mr.grid(row=row_mrc_labels, column=next_column, columnspan=cs)
        list_mrc_labels.append(label_mr)
        next_column += cs + 1


def separator_functions(self):
    toggle_label_color(self)
    adjust_colspan()


for sep in list_separator_labels:
    sep.bind('<ButtonRelease-1>', separator_functions)


def get_ep_options():
    dict_ep_options = {
        'str_unit': var_unit.get(),
        'bool_result': var_result.get()
    }
    return dict_ep_options


def get_quote_options():
    dict_quote_options = {
        'list_separators': get_separators(),
        'str_heading': var_heading.get()
    }
    return dict_quote_options


def get_weighted_options():
    dict_weighted_options = {
        'str_wwt_style': var_wwt_style.get(),
        'bool_total_col': var_total_col.get(),
        'bool_total_row': var_total_row.get()
    }
    return dict_weighted_options


def run_quote(self):
    if btn_quote['state'] == 'normal' or 'active':
        dict_ep_options = get_ep_options()
        dict_quote_options = get_quote_options()
        ep_scripts.calc_quote(var_files.get(), dict_ep_options, dict_quote_options)


btn_quote.bind('<ButtonRelease-1>', run_quote)


def run_weighted(self):
    dict_ep_options = get_ep_options()
    dict_weighted_options = get_weighted_options()
    if btn_weighted['state'] == 'normal' or 'active':
        ep_scripts.calc_weighted(var_files.get(), dict_ep_options, dict_weighted_options)


btn_weighted.bind('<ButtonRelease-1>', run_weighted)


def run_folder(self):
    if btn_folder['state'] == 'normal' or 'active':
        ep_scripts.open_folder(var_files.get())


btn_folder.bind('<ButtonRelease-1>', run_folder)


def select_and_focus(self):
    self.widget.select()
    self.widget.focus()


all_rbs = rbs_unit + rbs_heading + rbs_wwt_style
for rb in all_rbs:
    rb.bind('<ButtonRelease-1>', select_and_focus)


def file_selected(var, unknown, w):
    if var_files.get():
        btn_quote['state'] = 'normal'
        btn_weighted['state'] = 'normal'
        btn_folder['state'] = 'normal'
    else:
        btn_quote['state'] = 'disabled'
        btn_weighted['state'] = 'disabled'
        btn_folder['state'] = 'disabled'


var_files.trace('w', file_selected)


def return_to_click(self):
    tk_F.focus_get().event_generate('<ButtonRelease-1>')


root.bind('<Return>', return_to_click)
adjust_colspan()

top = tk_F.winfo_toplevel()
top.resizable(False, False)
print('tk window is ready to use.')
tk_F.mainloop()
