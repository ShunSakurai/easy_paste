'''
cd dropbox/codes/easy_paste
py ep_scripts.py
'''
import setup
import csv
import os
import os.path
import re
import subprocess
import sys
import urllib.request as ur
import webbrowser

# Constants
encodings = ['utf-16', 'utf-8-sig']

dict_csv_indices = {
    # Lower to higher match rates
    # (Context TM,) Repetitions, 100% Matches, 95% - 99%, 85% - 94%, 75% - 84%, 50% - 74%, No Match(, Total)
    'trados': [32, 28, 24, 20, 16, 12, 8],
    # (X-translated, 101%,) Repetitions, 100%, 95% - 99%, 85% - 94%, 75% - 84%, 50% - 74%, No match(, Fragments, Total)
    'all': [67, 59, 51, 43, 35, 27, 19]
}


# Strings and function to use for quote
tuple_str_mr = (('New', 'New'), ('50', '74%'), ('75', '84%'), ('85', '94%'), ('95', '99%'), ('100%', '100%'), ('Reps', 'Reps'))
quote_headers_display = [
    (r'New-(74|84|94|99)%', 'New'),
    (r'50-(84|94)%', 'Low Fuzzy'),
    (r'(50|75)-99%', 'Fuzzy'),
    (r'75-94%', 'Mid Fuzzy'),
    (r'85-99%', 'High Fuzzy'),
    # Look behind doesn't work when compiled and used in sub
    (r'50-Reps', r'50%-Reps'),
    (r'75-Reps', r'75%-Reps'),
    (r'85-Reps', r'85%-Reps'),
    (r'95-Reps', r'95%-Reps')
]
qh_display_for_replace = [(re.compile(t[0]), t[1]) for t in quote_headers_display]

qh_dexport_for_replace = [
    ('New', 'New Words'),
    ('Fuzzy', 'Fuzzy Matches'),
    ('100%-Reps', 'Repetitions and 100% Matches'),
    ('%', '% Matches'),
    ('Reps', 'Repetitions')
]


def replace_all_regex(string):
    for t in qh_display_for_replace:
        if t[0].match(string):
            return t[0].sub(string, t[1])
    return string


def replace_all_string(string):
    for t in qh_dexport_for_replace:
        if t[0] in string:
            return string.replace(t[0], t[1])
    return string


def return_mrc_colspan(list_separators):
    list_count = []
    count = 0
    for i in list_separators:
        if i:
            list_count.append(count)
            count = 0
        else:
            count += 1
    list_count.append(count)
    to_return = [i * 2 + 1 for i in list_count]
    return to_return


def return_mrc_text(list_separators):
    list_heading = []
    current_start = tuple_str_mr[0][0]
    for i in range(len(list_separators)):
        if list_separators[i]:
            list_heading.append('-'.join(unique_ordered_list((current_start, tuple_str_mr[i][1]))))
            current_start = tuple_str_mr[i + 1][0]
    list_heading.append('-'.join(unique_ordered_list((current_start, tuple_str_mr[-1][1]))))
    list_heading = [replace_all_regex(i) for i in list_heading]
    return list_heading


def return_slice_group_quote(dict_quote_options):
    r'''
    >>> return_slice_group_quote({'list_separators': [False, True, False, False, True, False]})
    [[0, 2], [2, 5], [5, 7]]
    '''
    list_separators = dict_quote_options['list_separators']
    source_slice_groups_quote = tuple((i, i + 1) for i in range(7))
    to_return = []
    current_start = source_slice_groups_quote[0][0]
    for i in range(len(list_separators)):
        if list_separators[i]:
            to_return.append([current_start, source_slice_groups_quote[i][1]])
            current_start = source_slice_groups_quote[i + 1][0]
    to_return.append([current_start, source_slice_groups_quote[-1][1]])
    return to_return


def return_heading_quote(dict_quote_options):
    list_heading = return_mrc_text(dict_quote_options['list_separators'])
    list_heading = [replace_all_string(i) for i in list_heading]
    if dict_quote_options['str_heading'] == 'long':
        list_heading = ['Translation - ' + h  for h in list_heading]
    return list_heading


# Strings and function to use for weighted words
list_slice_groups_weighted = [[i, i + 1] for i in range(6, -1, -1)]
# [[6, 7], [5, 6], [4, 5], [3, 4], [2, 3], [1, 2], [0, 1]]

row_1 = ['Check 100% matches:', 'Yes']
row_2 = ['Chargeable words per day:', 2000]
row_3 = ['Apply MT:', 'Yes']
row_5_time = [
    'Item', 'Wds', 'TrHrs', 'PrHrs', 'MaxHrs', 'DueDate',
    'Reps', '100%', '95-99%', '85-94%', '75-84%', '50-74%', 'New']
row_5_words = [
    'Item', 'Repeated', '100%', '95-99%', '85-94%', '75-84%', '50-74%', 'No Match',
    'Translation time', 'Proofreading time', 'Total time (hours)', 'Chargeable words']
row_5_total = ['', 'TrHrs Subtotal', 'PrHrs Subtotal']
c = 'ABCDEFGHIJKLM'
start_row = 6

fname_template = 'files/Analysis-Template.csv'
pattern_slice_end = re.compile(r'^(.+):\s(\d+)\-\d+$')
pattern_slice_middle = re.compile(r'^(\[.+\]).*?\[(\d+)\-\d+\](.+)$')


# Utility classes and functions
class FileTypeError(Exception):
    def __str__(self):
        return 'File type not supported. See readme for the supported files.'


def add_num_in_2d_list(md_list, num):
    r'''
    >>> add_num_in_2d_list([[67], [35, 43, 51, 59], [27], [19]], 1)
    [[68], [36, 44, 52, 60], [28], [20]]
    '''
    for i in range(len(md_list)):
        md_list[i] = [j + 1 for j in md_list[i]]
    return md_list


def addup_unit(row, index_list):
    unit_sum = 0
    for i in index_list:
        unit_sum += int(row[i])
    return unit_sum


def check_updates():
    print('-' * 70)
    url_releases = 'https://github.com/ShunSakurai/easy_paste/releases'
    try:
        str_release_page = str(ur.urlopen(url_releases).read())
    except:
        print('Easy Paste could not connect to', url_releases)
        return
    pattern_version = re.compile(r'(?<=<span class="css-truncate-target">v)[0-9.]+(?=</span>)')
    pattern_installer = re.compile(r'/ShunSakurai/easy_paste/releases/download/v([0-9.]+)/(easy_paste_installer_\1.0.exe)')
    str_newest_version = pattern_version.search(str_release_page).group(0)
    url_installer = pattern_installer.search(str_release_page)
    if new_version_is_available(setup.dict_console['version'], str_newest_version):
        download_update(str_newest_version, url_installer)
    else:
        print('You are using the newest version:', setup.dict_console['version'])
        return


def detect_file_type_and_delimiter(dict_ep_options, fn):
    delimiter = ''
    csv_indices = ''
    for enc in encodings:
        f = open(fn, encoding=enc)
        try:
            content = f.readline()
        except UnicodeDecodeError:
            continue
        delimiter = content[0]
        if 'X-translated' in content:
            csv_indices = dict_csv_indices['all']
        elif 'Context TM' in content and dict_ep_options['str_unit'] == 'word':
            csv_indices = dict_csv_indices['trados']
        else:
            print('-' * 70)
            if 'Context TM' in content and dict_ep_options['str_unit'] == 'char':
                print(
                    'Trados Compatible CSV doesn\'t support Characters.\n',
                    'Please use another format.\n')
            raise FileTypeError()
        return csv_indices, enc, delimiter


def dir_from_str_path(str_path):
    r'''
    >>> dir_from_str_path('C:\\easy_paste\\files\\Analysis-GitHub Readme.csv')
    'C:/easy_paste/files'
    '''
    str_path = replace_bslash_w_fslash(str_path)
    if str_path.endswith('/'):
        str_path_dir = str_path.rstrip('/')
    elif '.' in str_path.rsplit('/', 1)[-1]:
        str_path_dir = str_path.rsplit('/', 1)[0]
    else:
        str_path_dir = str_path
    return str_path_dir


def divide_str_tuple(str_tuple):
    r'''
    >>> divide_str_tuple(r"('/Users/path/csv.csv', '/Users/path/file name with space.txt',)")
    ['/Users/path/csv.csv', '/Users/path/file name with space.txt']
    '''
    if str_tuple[0] == '(':
        # file is selected from the button
        for (old, new) in [('(\'', '{'), ('\',', '}'), ('\')', '}'), ('\'', '{')]:
            str_tuple = str_tuple.replace(old, new)
    else:
        # file is input directly in the field
        # assuming only one file is selected
        str_tuple = ''.join(['{', str_tuple, '}'])
    list_from_str = []

    while str_tuple:
        if str_tuple[0] == '{':
            end = str_tuple.find('}') + 1
        else:
            end = str_tuple.find(' ', 1)

        if end == -1:
            list_from_str.append(str_tuple)
            break
        else:
            list_from_str.append(str_tuple[: end])
            str_tuple = str_tuple[end + 1:]

    list_from_str_clean = [i.strip(' {},"\'') for i in list_from_str]
    return list_from_str_clean


def download_update(str_newest_version, url_installer):
    print('Downloading the newest version', str_newest_version)
    print('Your version is', setup.dict_console['version'])
    download_folder = os.path.expanduser("~")+'/Downloads/'
    download_path = download_folder + url_installer.group(2)
    d = ur.urlopen('https://github.com/' + url_installer.group(0))
    with open(download_path, 'wb') as f:
        f.write(d.read())
    print('Starting the installer.')
    if sys.platform.startswith('win'):
        download_path = replace_fslash_w_bslash(download_path)
        os.startfile(download_path)
    else:
        subprocess.run(['open', download_path])
    return


def get_next_grid_row(root):
    return root.grid_size()[1] + 1


def insert_prefix_in_path(str_file_path, prefix):
    str_file_path = replace_bslash_w_fslash(str_file_path)
    analysis_divided = str_file_path.rsplit('/', 2)
    part_path = ''.join([
        analysis_divided[1], prefix, analysis_divided[2]])
    full_path = ''.join([
        analysis_divided[0], '/', part_path])
    return full_path, part_path


def new_version_is_available(str_installed, str_online):
    list_installed = setup.zero_pad(str_installed).split('.')
    list_online = setup.zero_pad(str_online).split('.')
    for (i, o) in zip(list_installed, list_online):
        if int(i) == int(o):
            pass
        else:
            return int(i) < int(o)
    return False


def open_file(str_file_path):
    try:
        if sys.platform.startswith('win'):
            str_file_path = replace_fslash_w_bslash(str_file_path)
            os.startfile(str_file_path)
        else:
            subprocess.run(['open', str_file_path])
    except (FileNotFoundError, PermissionError):
        print('File could not be opened from inside Easy Paste.')
        print('Please go to the file location and open it manually.')
        print(sys.exc_info()[1])


def open_readme():
    webbrowser.open_new_tab(
        'https://github.com/ShunSakurai/easy_paste/blob/master/README.md')


def print_success(path):
    print('-' * 70, '\n\rSuccessfully created:\n', path, sep='')


def print_end():
    print('\nClick [x] on the tk window to close the program.')


def replace_bslash_w_fslash(str_path):
    return str_path.replace('\\', '/')


def replace_fslash_w_bslash(str_path):
    return str_path.replace('/', '\\')


def return_half_row(l):
    return ['\'1/2'] + [''.join(['=', c[i], str(l + 2), '/2']) for i in range(1, 4)]


def return_total_row(l):
    return ['Total'] + [''.join(['=sum(', c[i], str(start_row), ':', c[i], str(l), ')']) for i in range(1, 13)]


def return_weighted_equations_time(r, dict_weighted_options):
    translation_time = ''.join([
        '=(((', c[8], r, '+', c[9], r, ')*0.25)+(', c[10], r, '*0.60)+(',
        c[11], r, '+', c[12], r, ')*(1-0.2*(B$3="Yes")))/', c[1], '$2*8*4/5'])
    proof_time = ''.join([
        '=(((',
        c[6], r, '+', c[7], r, ')*(1+2*(B$1="Yes"))/3+(',
        c[8], r, '+', c[9], r, ')*0.25)+(', c[10], r, '*0.60)+',
        c[11], r, '+', c[12], r, ')/', c[1], '$2*8/5'])
    total_time = ''.join(['=SUM(', c[2], r, ':', c[3], r, ')'])
    weighted_words = ''.join(['=', c[4], r, '*(', c[1], '$2/8)'])
    equations = [weighted_words, translation_time, proof_time, total_time]
    return equations


def return_weighted_equations_words(r, dict_weighted_options):
    translation_time = ''.join([
        '=(((', c[3], r, '+', c[4], r, ')*0.25)+(', c[5], r, '*0.60)+(',
        c[6], r, '+', c[7], r, ')*(1-0.2*(B$3="Yes")))/B$2*8*4/5'])
    proof_time = ''.join([
        '=(((',
        c[1], r, '+', c[2], r, ')*(1+2*(B$1="Yes"))/3+(',
        c[3], r, '+', c[4], r, ')*0.25)+(', c[5], r, '*0.60)+',
        c[6], r, '+', c[7], r, ')/B$2*8/5'])
    total_time = ''.join(['=SUM(', c[8], r, ':', c[9], r, ')'])
    weighted_words = ''.join(['=', c[10], r, '*(B$2/8)'])
    equations = [translation_time, proof_time, total_time, weighted_words]
    return equations


def return_total_equations_time(r):
    trhrs_subtotal = ''.join(['=sum(', c[2], '$', str(start_row), ':', c[2], r, ')'])
    prhrs_subtotal = ''.join(['=sum(', c[3], '$', str(start_row), ':', c[3], r, ')'])
    return ['', trhrs_subtotal, prhrs_subtotal]


def return_total_equations_words(r):
    trhrs_subtotal = ''.join(['=sum(', c[8], '$', str(start_row), ':', c[8], r, ')'])
    prhrs_subtotal = ''.join(['=sum(', c[9], '$', str(start_row), ':', c[9], r, ')'])
    return ['', trhrs_subtotal, prhrs_subtotal]


def shorten_fname(file_path):
    r'''
    >>> shorten_fname(r'[jpn] "Z:\Users\sakuraishun\Dropbox\Codes\easy_paste\README.md"')
    '[jpn]README.md'
    '''
    file_path = replace_bslash_w_fslash(file_path)
    lan = ''
    if '.' in file_path and '/' in file_path:
        if file_path.startswith('['):
            lan = file_path[:file_path.find(']') + 1]
            fname = file_path.rsplit('/', 1)[1].strip('"')
        else:
            fname = file_path.rsplit('/', 1)[1]
    else:
        fname = file_path
    return lan + fname


def slice_indices(csv_indices, slice_group):
    r'''
    >>> slice_indices([67, 59, 51, 43, 35, 27, 19], [[0, 2], [2, 5], [5, 6], [6, 7]])
    [[67, 59], [51, 43, 35], [27], [19]]
    '''
    csv_indices_grouped = []
    for group in slice_group:
        csv_indices_grouped.append(csv_indices[group[0]:group[1]])
    return csv_indices_grouped


def sort_slices(lines):
    r'''
    >>> sort_slices([['File A: 1-90', '1'], ['File A: 181-270', '1'], ['File B', '1'], ['File A: 91-180', '1']])
    [['File A: 1-90', '1'], ['File A: 91-180', '1'], ['File A: 181-270', '1'], ['File B', '1']]
    '''
    dict_sliced_files = {}
    for i in range(len(lines)):
        full_fname = lines[i][0]
        match_end = pattern_slice_end.match(full_fname)
        match_middle = pattern_slice_middle.match(full_fname)

        if match_end or match_middle:
            if match_end:
                base_fname, start = match_end.group(1), int(match_end.group(2))
            else:
                base_fname = match_middle.group(1) + match_middle.group(3)
                start = int(match_middle.group(2))

            if base_fname not in dict_sliced_files:
                dict_sliced_files[base_fname] = [{'idx': i, 'start': start}]
            else:
                dict_sliced_files[base_fname].append({'idx': i, 'start': start})
                list_idx_start = dict_sliced_files[base_fname]
                for j in range(len(list_idx_start) - 1):
                    if list_idx_start[j]['start'] > start:
                        idx_in_lines = list_idx_start[j]['idx']
                        lines.insert(idx_in_lines, lines.pop(i))
                        list_idx_start.insert(j, list_idx_start.pop())
                        list_idx_start[j]['idx'] = idx_in_lines
                        for k in range(j + 1, len(list_idx_start)):
                            list_idx_start[k]['idx'] += 1
                        break
    return lines


def subtotal_by_lang(list_combined, list_quote_line, num_items):
    lan = list_quote_line[0][1:list_quote_line[0].find(']')]
    if list_combined and list_combined[-1][0] == lan:
        for i in range(num_items):
            list_combined[-1][i + 1] += list_quote_line[i + 1]
    else:
        list_combined.append([lan] + list_quote_line[1:])
    return list_combined


def unique_ordered_list(sequence):
    unique_list = []
    for i in sequence:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


def write_lines_to_full_path(full_path, lines):
    result_file = open(full_path, 'w', encoding='utf-8')
    result_writer = csv.writer(result_file, delimiter=',', lineterminator='\n')
    result_writer.writerows(lines)
    result_file.close()


# Main functions
def provide_quote_lines(analysis_read, csv_indices, headings):
    num_items = len(csv_indices)
    list_quote_lines = []
    list_combined = []
    next(analysis_read)
    next(analysis_read)
    for row in analysis_read:
        list_quote_line = []
        fname = shorten_fname(row[0])
        list_quote_line.append(fname)
        for i in range(num_items):
            unit_sum = addup_unit(row, csv_indices[i])
            list_quote_line.append(unit_sum)
        list_quote_lines.append(list_quote_line)

        if fname.startswith('['):
            list_combined = subtotal_by_lang(list_combined, list_quote_line, num_items)

    lines = []
    separator = '\'' + '=' * 20
    if list_combined:
        list_quote_lines = [[separator], ['Total per language']] + list_combined + [[separator], ['Individual files']] + list_quote_lines

    for list_quote_line in list_quote_lines:
        lines.append([list_quote_line[0]])
        if len(list_quote_line) >= 2:
            for i in range(num_items):
                lines.append([headings[i], list_quote_line[i + 1]])
        lines.append([''])
    return lines


def provide_weighted_lines(analysis_read, csv_indices, dict_weighted_options):
    if dict_weighted_options['str_wwt_style'] == 'time_first':
        row_5, func_equation, func_total = row_5_time, return_weighted_equations_time, return_total_equations_time
    elif dict_weighted_options['str_wwt_style'] == 'words_first':
        row_5, func_equation, func_total = row_5_words, return_weighted_equations_words, return_total_equations_words
    if dict_weighted_options['bool_total_col']:
        row_5 = row_5 + row_5_total
    header_lines = [row_1, row_2, row_3, [''], row_5]
    next(analysis_read)
    next(analysis_read)
    num_row = start_row - 1

    orig_body_lines = [row for row in analysis_read]
    body_lines = []
    for row in orig_body_lines:
        num_row += 1
        fname = shorten_fname(row[0])
        list_words = [addup_unit(row, csv_indices[i]) for i in range(len(csv_indices))]
        list_equations = func_equation(str(num_row), dict_weighted_options)
        if dict_weighted_options['str_wwt_style'] == 'time_first':
            row_body = [fname] + list_equations + [''] + list_words
        elif dict_weighted_options['str_wwt_style'] == 'words_first':
            row_body = [fname] + list_words + list_equations
        body_lines.append(row_body)

    sorted_body_lines = sort_slices(body_lines)

    if dict_weighted_options['bool_total_col']:
        num_row = start_row - 1
        for row_body in sorted_body_lines:
            num_row += 1
            row_body += func_total(str(num_row))

    total_lines = []
    if dict_weighted_options['bool_total_row']:
        length = len(header_lines) + len(body_lines)
        total_lines.append([''])
        total_lines.append(return_total_row(length))
        total_lines.append(return_half_row(length))

    return header_lines + body_lines + total_lines


def calc_quote(str_files, dict_ep_options, dict_quote_options):
    for str_file_path in divide_str_tuple(str_files):
        indices, enc, dl = detect_file_type_and_delimiter(dict_ep_options, str_file_path)
        csv_indices = slice_indices(indices, return_slice_group_quote(dict_quote_options))
        headings = return_heading_quote(dict_quote_options)
        if dict_ep_options['str_unit'] == 'char':
            csv_indices = add_num_in_2d_list(csv_indices, 1)
        analysis_read = csv.reader(
            open(str_file_path, encoding=enc), delimiter=dl)
        prefix = ''.join(['/quote-', dict_ep_options['str_unit'], '-'])
        full_path, part_path = insert_prefix_in_path(str_file_path, prefix)

        str_options = 'Easy Paste Options:' + dict_ep_options['str_unit']
        print(str_options)
        lines = [[str_options], ['']] + provide_quote_lines(analysis_read, csv_indices, headings)
        write_lines_to_full_path(full_path, lines)
        print_success(part_path)
        if dict_ep_options['bool_result']:
            open_file(full_path)
    print_end()


def calc_weighted(str_files, dict_ep_options, dict_weighted_options):
    for str_file_path in divide_str_tuple(str_files):
        indices, enc, dl = detect_file_type_and_delimiter(dict_ep_options, str_file_path)
        csv_indices = slice_indices(indices, list_slice_groups_weighted)
        if dict_ep_options['str_unit'] == 'char':
            csv_indices = add_num_in_2d_list(csv_indices, 1)
        analysis_read = csv.reader(
            open(str_file_path, encoding=enc), delimiter=dl)
        prefix = ''.join(['/weighted-', dict_ep_options['str_unit'], '-'])
        full_path, part_path = insert_prefix_in_path(str_file_path, prefix)

        lines = provide_weighted_lines(analysis_read, csv_indices, dict_weighted_options)
        write_lines_to_full_path(full_path, lines)
        print_success(part_path)
        if dict_ep_options['bool_result']:
            open_file(full_path)
    print_end()


def export_template(full_path, dict_ep_options, dict_weighted_options):
    indices, enc, dl = detect_file_type_and_delimiter(dict_ep_options, fname_template)
    csv_indices = slice_indices(dict_csv_indices['all'], list_slice_groups_weighted)
    analysis_read = csv.reader(
        open(fname_template, encoding=enc), delimiter=dl)
    lines = provide_weighted_lines(analysis_read, csv_indices, dict_weighted_options)
    write_lines_to_full_path(full_path, lines)
    if dict_ep_options['bool_result']:
        open_file(full_path)
    print_end()


def open_folder(str_files):
    str_file_path = divide_str_tuple(str_files)[0]
    analysis_divided = str_file_path.rsplit('/', 1)
    folder_full_path = analysis_divided[0]
    if sys.platform.startswith('win'):
        folder_full_path = replace_fslash_w_bslash(folder_full_path)
        os.startfile(folder_full_path)
    else:
        subprocess.run(['open', folder_full_path])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
