'''
cd dropbox/codes/easy_paste
py ep_scripts.py
'''
import csv

headings_joined = {
    'short': ['New Words', 'Fuzzy Matches', 'Repetitions and 100% Matches'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches', 'Translation -  Repetitions and 100% Matchs']}

headings_separate = {
    'short': ['New Words', 'Fuzzy Matches', '100% Matches', 'Repetitions'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches', 'Translation - 100% Matchs', 'Translation -  Repetitions']}

csv_indices_joined = [[32], [16, 20, 24, 28], [4, 8, 12]]
csv_indices_separate = [[32], [16, 20, 24, 28], [12], [4, 8]]


def addup_unit(row, index_list):
    unit_sum = 0
    for i in index_list:
        unit_sum += int(row[i])
    return unit_sum


def detect_delimiter(fn):
    f = open(fn, encoding='utf-16')
    delimiter = f.read()[0]
    return delimiter


def get_fname(lan_path):
    r'''
    >>> get_fname(r'[jpn] "Z:\Users\sakuraishun\Dropbox\Codes\easy_paste\README.md"')
    '[jpn]README.md'
    '''
    if lan_path.startswith('['):
        lan = lan_path[:lan_path.find(']') + 1]
        fname = lan + lan_path.rsplit('\\', 1)[1].strip('"')
        return fname
    else:
        fname = lan_path.rsplit('\\', 1)[1]
        return fname


def calc_csv(analysis_read, var_rep100, var_heading):
    if var_rep100.get() == 'joined':
        csv_indices = csv_indices_joined
        headings = headings_joined
    if var_rep100.get() == 'separate':
        csv_indices = csv_indices_separate
        headings = headings_separate
    lines = []
    for row in analysis_read:
        if len(row[0].rsplit('.', 1)) == 1:
            pass
        else:
            fname = get_fname(row[0])
            lines.append([fname])
            for i in range(len(csv_indices)):
                label_sum = headings[var_heading.get()][i]
                unit_sum = addup_unit(row, csv_indices[i])
                lines.append([label_sum, unit_sum])
            lines.append(['\n'])
    return lines


def calc_sum(var_file, var_rep100, var_heading):
    analysis_path = var_file.get()
    dl = detect_delimiter(analysis_path)
    analysis_read = csv.reader(open(analysis_path, encoding='utf-16'), delimiter=dl)

    analysis_divided = analysis_path.rsplit('/', 2)
    quote_full_path = analysis_divided[0] + '/' + analysis_divided[1] + '/to_paste(utf-8, comma)' + analysis_divided[2]
    quote_part_path = analysis_divided[1] + '/to_paste(utf-8, comma)' + analysis_divided[2]

    quote = open(quote_full_path, 'a', encoding='utf-8')
    quote_write = csv.writer(quote, delimiter=',', lineterminator='\n')
    lines = calc_csv(analysis_read, var_rep100, var_heading)
    quote_write.writerows(lines)
    quote.close()

    print('\nSuccessfully created:\n' + quote_part_path + '\n' +
          'Click [x] on the tk window and close the program.')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
