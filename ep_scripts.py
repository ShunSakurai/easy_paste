'''
cd dropbox/codes/easy_paste
py ep_scripts.py
'''
import csv
import os
import subprocess
import sys

csv_indices_joined = [[32], [16, 20, 24, 28], [4, 8, 12]]
csv_indices_separate = [[32], [16, 20, 24, 28], [12], [4, 8]]
csv_indices_weighted = [[4, 8], [12], [16], [20], [24], [28], [32]]

# Strings to use for quotes
headings_joined = {
    'short': ['New Words', 'Fuzzy Matches', 'Repetitions and 100% Matches'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches',
             'Translation -  Repetitions and 100% Matchs']}

headings_separate = {
    'short': ['New Words', 'Fuzzy Matches', '100% Matches', 'Repetitions'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches',
             'Translation - 100% Matchs', 'Translation -  Repetitions']}

# Strings and function to use for weighted words
row_1 = [r'If check 100% match is No, delete values in Repeated and 100%']
row_2 = ['Chargeable words per day (can be changed) :', 2000, '', '', '', '', '']
row_3 = [
    'Item', 'Repeated', '100%', '95-99%', '85-94%', '75-84%', '50-74%', 'No Match',
    'Translation time', 'Proofreading time', 'Total time (hours)', 'Chargeable words']
c = 'ABCDEFGHIJKLM'


def return_equations(r):
    translation_time = ''.join([
        '=(((', c[3], r, '+', c[4], r, ')*0.25)+(', c[5], r, '*0.60)+',
        c[6], r, '+', c[7], r, ')/B$2*', r, '*4/5'])
    proof_time = ''.join([
        '=(((', c[3], r, '+', c[4], r, ')*0.25)+(', c[5], r, '*0.60)+',
        c[1], r, '+', c[2], r, '+', c[6], r, '+', c[7], r, ')/B$2*', r, '/5'])
    total_time = ''.join(['=SUM(', c[8], r, ':', c[9], r, ')'])
    weighted_words = ''.join(['=', c[10], r, '*(B$2/', r, ')'])
    return [translation_time, proof_time, total_time, weighted_words]


def addup_unit(row, index_list):
    unit_sum = 0
    for i in index_list:
        unit_sum += int(row[i])
    return unit_sum


def detect_delimiter(fn):
    f = open(fn, encoding='utf-16')
    delimiter = f.read()[0]
    return delimiter


def print_success(path):
    print('\n', '-' * 70, '\nSuccessfully created:\n', path)
    print('\nClick [x] on the tk window to close the program.')


def shorten_fname(file_name):
    r'''
    >>> shorten_fname(r'[jpn] "Z:\Users\sakuraishun\Dropbox\Codes\easy_paste\README.md"')
    '[jpn]README.md'
    '''
    if '.' in file_name and file_name.startswith('['):
        lan = file_name[:file_name.find(']') + 1]
        fname = lan + file_name.rsplit('\\', 1)[1].strip('"')
        return fname
    elif '.' in file_name:
        fname = file_name.rsplit('\\', 1)[1]
        return fname
    else:
        fname = file_name
        return fname


def quote_content(analysis_read, var_rep100, var_heading):
    if var_rep100.get() == 'joined':
        csv_indices = csv_indices_joined
        headings = headings_joined
    if var_rep100.get() == 'separate':
        csv_indices = csv_indices_separate
        headings = headings_separate
    lines = []
    next(analysis_read)
    next(analysis_read)
    for row in analysis_read:
        fname = shorten_fname(row[0])
        lines.append([fname])
        for i in range(len(csv_indices)):
            label_sum = headings[var_heading.get()][i]
            unit_sum = addup_unit(row, csv_indices[i])
            lines.append([label_sum, unit_sum])
        lines.append(['\n'])
    return lines


def calc_quote(var_file, var_rep100, var_heading):
    analysis_path = var_file.get()
    dl = detect_delimiter(analysis_path)
    analysis_read = csv.reader(open(analysis_path, encoding='utf-16'), delimiter=dl)
    analysis_divided = analysis_path.rsplit('/', 2)
    full_path = ''.join([analysis_divided[0], '/', analysis_divided[1], '/to_paste(utf-8, comma)', analysis_divided[2]])
    part_path = ''.join([analysis_divided[1], '/to_paste(utf-8, comma)', analysis_divided[2]])

    lines = quote_content(analysis_read, var_rep100, var_heading)

    quote_file = open(full_path, 'w', encoding='utf-8')
    quote_write = csv.writer(quote_file, delimiter=',', lineterminator='\n')
    quote_write.writerows(lines)
    quote_file.close()

    print_success(part_path)


def calc_weighted(var_file):
    analysis_path = var_file.get()
    dl = detect_delimiter(analysis_path)
    analysis_read = csv.reader(
        open(analysis_path, encoding='utf-16'), delimiter=dl)
    analysis_divided = analysis_path.rsplit('/', 2)
    full_path = ''.join([
        analysis_divided[0], '/', analysis_divided[1],
        '/weighted_', analysis_divided[2]])
    part_path = ''.join([
        analysis_divided[1], '/weighted_', analysis_divided[2]])

    csv_indices = csv_indices_weighted

    lines = []
    for i in [row_1, row_2, row_3]:
        lines.append(i)
    next(analysis_read)
    next(analysis_read)
    row_num = 3
    for row in analysis_read:
        row_num += 1
        r = str(row_num)
        fname = shorten_fname(row[0])
        words = [addup_unit(row, csv_indices[i]) for i in range(len(csv_indices))]
        equations = return_equations(r)
        lines.append([fname] + words + equations)

    weighted_file = open(full_path, 'w', encoding='utf-8')
    quote_write = csv.writer(weighted_file, delimiter=',', lineterminator='\n')
    quote_write.writerows(lines)
    weighted_file.close()

    print_success(part_path)


def open_folder(var_file):
    analysis_path = var_file.get()
    analysis_divided = analysis_path.rsplit('/', 1)
    folder_full_path = analysis_divided[0]
    if sys.platform.startswith('win'):
        os.startfile(folder_full_path)
    else:
        subprocess.call(['open', folder_full_path])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
