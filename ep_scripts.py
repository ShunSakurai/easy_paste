'''
cd dropbox/codes/easy_paste
py ep_scripts.py
'''
import csv
import os
import subprocess
import sys

encodings = ['utf-16', 'utf-8']

csv_indices_trados = [4, 8, 12, 16, 20, 24, 28, 32]
csv_indices_all = [11, 19, 27, 35, 43, 51, 59, 67]

slice_group_joined = [[7, 8], [3, 7], [0, 3]]
slice_group_separate = [[7, 8], [3, 7], [2, 3], [0, 2]]
slice_group_weighted = [[0, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]

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
    'Item', 'Wds', 'TrHrs', 'PrHrs', 'MaxHrs', 'DueDate',
    'Reps', '100%', '95-99%', '85-94%', '75-84%', '50-74%', 'New']
c = 'ABCDEFGHIJKLM'


# Utility functions
def addup_unit(row, index_list):
    unit_sum = 0
    for i in index_list:
        unit_sum += int(row[i])
    return unit_sum


def detect_file_type_and_delimiter(fn):
    delimiter = ''
    for enc in encodings:
        try:
            f = open(fn, encoding=enc)
            content = f.readline()
            delimiter = content[0]
            if 'Context TM' in content:
                csv_indices = csv_indices_trados
            elif 'X-translated' in content:
                csv_indices = csv_indices_all
            return csv_indices, enc, delimiter
        except:
            pass
    if not delimiter:
        print('File type and delimiter could not be identified.')


def get_paths_to_write(str_file_path, prefix):
    analysis_divided = str_file_path.rsplit('/', 2)
    part_path = ''.join([
        analysis_divided[1], prefix, analysis_divided[2]])
    full_path = ''.join([
        analysis_divided[0], '/', part_path])
    return full_path, part_path


def print_success(path):
    print('\n', '-' * 70, '\nSuccessfully created:\n', path)
    print('\nClick [x] on the tk window to close the program.')


def return_weighted_equations(r):
    translation_time = ''.join([
        '=(((', c[8], r, '+', c[9], r, ')*0.25)+(', c[10], r, '*0.60)+',
        c[11], r, '+', c[12], r, ')/', c[1], '$2*8*4/5'])
    proof_time = ''.join([
        '=(((', c[8], r, '+', c[9], r, ')*0.25)+(', c[10], r, '*0.60)+',
        c[6], r, '+', c[7], r, '+', c[11], r, '+', c[12], r, ')/', c[1], '$2*8/5'])
    total_time = ''.join(['=SUM(', c[2], r, ':', c[3], r, ')'])
    weighted_words = ''.join(['=', c[4], r, '*(', c[1], '$2/8)'])
    return [weighted_words, translation_time, proof_time, total_time]


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


def slice_indices(csv_indices, slice_group):
    csv_indices_grouped = []
    for group in slice_group:
        csv_indices_grouped.append(csv_indices[group[0]:group[1]])
    return csv_indices_grouped


def write_lines_to_full_path(full_path, lines):
    result_file = open(full_path, 'w', encoding='utf-8')
    result_writer = csv.writer(result_file, delimiter=',', lineterminator='\n')
    result_writer.writerows(lines)
    result_file.close()


# Main functions
def provide_quote_lines(analysis_read, csv_indices, headings):
    lines = []
    next(analysis_read)
    next(analysis_read)
    for row in analysis_read:
        fname = shorten_fname(row[0])
        lines.append([fname])
        for i in range(len(csv_indices)):
            label_sum = headings[i]
            unit_sum = addup_unit(row, csv_indices[i])
            lines.append([label_sum, unit_sum])
        lines.append(['\n'])
    return lines


def provide_weighted_lines(analysis_read, csv_indices):
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
        equations = return_weighted_equations(r)
        lines.append([fname] + equations + [''] + words)
    return lines


def calc_quote(str_file_path, str_rep100, str_heading):
    indices, enc, dl = detect_file_type_and_delimiter(str_file_path)
    if str_rep100 == 'joined':
        csv_indices = slice_indices(indices, slice_group_joined)
        headings = headings_joined[str_heading]
    if str_rep100 == 'separate':
        csv_indices = slice_indices(indices, slice_group_separate)
        headings = headings_separate[str_heading]
    analysis_read = csv.reader(
        open(str_file_path, encoding=enc), delimiter=dl)
    full_path, part_path = get_paths_to_write(str_file_path, '/to_paste(utf-8, comma)')

    lines = provide_quote_lines(analysis_read, csv_indices, headings)
    write_lines_to_full_path(full_path, lines)
    print_success(part_path)


def calc_weighted(str_file_path):
    indices, enc, dl = detect_file_type_and_delimiter(str_file_path)
    csv_indices = slice_indices(indices, slice_group_weighted)
    analysis_read = csv.reader(
        open(str_file_path, encoding=enc), delimiter=dl)
    full_path, part_path = get_paths_to_write(str_file_path, '/weighted_')

    lines = provide_weighted_lines(analysis_read, csv_indices)
    write_lines_to_full_path(full_path, lines)
    print_success(part_path)


def open_folder(str_file_path):
    analysis_divided = str_file_path.rsplit('/', 1)
    folder_full_path = analysis_divided[0]
    if sys.platform.startswith('win'):
        os.startfile(folder_full_path)
    else:
        subprocess.call(['open', folder_full_path])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
