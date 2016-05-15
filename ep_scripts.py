import csv

headings_joined = {
    'short': ['New Words', 'Fuzzy Matches', 'Repetitions and 100% Matches'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches', 'Translation -  Repetitions and 100% Matchs']}

headings_separate = {
    'short': ['New Words', 'Fuzzy Matches', '100% Matches', 'Repetitions'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches', 'Translation - 100% Matchs'', Translation -  Repetitions']}

csv_indice_joined = [[32], [16, 20, 24, 28], [4, 8, 12]]
csv_indice_separate = [[32], [16, 20, 24, 28], [12], [4, 8]]


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
    '''
    >>> '[jpn] "Z:\\Users\\sakuraishun\\Dropbox\\Codes\\easy_paste\\README.md"''
    [jpn]README.md
    '''
    if lan_path.startswith('['):
        lan = lan_path[:lan_path.find(']') + 1]
        fname = lan + lan_path.rsplit('\\', 1)[1].strip('"')
        return fname
    else:
        fname = lan_path.rsplit('\\', 1)[1]
        return fname


def calc_csv(analysis_read, var_unit, var_rep100, var_heading):
    print(var_rep100.get())
    if var_unit.get() == 'word':
        pass
    elif var_unit.get() == 'char':
        raise ValueError('Trados-compatible CSV file doesn\'t contain characters. Please use the HTML format.')
    if var_rep100.get() == 'joined':
        csv_indice = csv_indice_joined
        headings = headings_joined
    if var_rep100.get() == 'separate':
        csv_indice = csv_indice_separate
        headings = headings_separate
    lines = []
    for row in analysis_read:
        if len(row[0].rsplit('.', 1)) == 1:
            pass
        else:
            fname = get_fname(row[0])
            lines.append([fname])
            for i in range(len(csv_indice)):
                label_sum = headings[var_heading.get()][i]
                unit_sum = addup_unit(row, csv_indice[i])
                lines.append([label_sum, unit_sum])
            lines.append(['\n'])
    return lines


def calc_html(analysis_read, var_unit, var_rep100, var_heading):
    pass


def calc_sum(var_file, var_unit, var_rep100, var_heading):
    analysis_path = var_file.get()
    if analysis_path.rsplit('.', 1)[1] == 'csv':
        dl = detect_delimiter(analysis_path)
        analysis_read = csv.reader(open(analysis_path, encoding='utf-16'), delimiter=dl)
        calc_file = calc_csv
    else:
        analysis_read = open(analysis_path, encoding='utf-8')
        calc_file = calc_html

    analysis_divided = analysis_path.rsplit('/', 2)
    quote_full_path = analysis_divided[0] + '/' + analysis_divided[1] + '/to_paste(utf-8, comma)' + analysis_divided[2]
    quote_part_path = analysis_divided[1] + '/to_paste(utf-8, comma)' + analysis_divided[2]

    quote = open(quote_full_path, 'a', encoding='utf-8')
    quote_write = csv.writer(quote, delimiter=',', lineterminator='\n')
    lines = calc_file(analysis_read, var_unit, var_rep100, var_heading)
    quote_write.writerows(lines)
    quote.close()

    print('Successfully created:\n' + quote_part_path + '\n' +
          'Click [x] on the tk window and close the program.\n')
