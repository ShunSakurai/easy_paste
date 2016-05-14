import csv

templates = {
    'short': ['New Words', 'Fuzzy Matches', 'Repetitions and 100% Matches'],
    'long': ['Translation -  New Words', 'Translation -  Fuzzy Matches', 'Translation -  Repetitions and 100% Matchs']}


def addup_unit(row, index_list):
    unit_sum = 0
    for i in index_list:
        unit_sum += int(row[i])
    return unit_sum
    print(unit_sum)


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
        fname = lan + lan_path.rsplit('\\', 1)[1]
        return fname
    else:
        fname = lan_path.rsplit('\\', 1)[1].strip('"')
        return fname


def calc_csv(analysis_read, var_unit, var_template):
    if var_unit.get() == 'word':
        analysis_indice = [[32], [16, 20, 24, 28], [4, 8, 12]]
    elif var_unit.get() == 'char':
        raise ValueError('Trados-compatible CSV file doesn\'t contain characters. Please use the HTML format.')
    lines = []
    for row in analysis_read:
        if len(row[0].rsplit('.', 1)) == 1:
            pass
        else:
            fname = get_fname(row[0])
            sum_new = addup_unit(row, analysis_indice[0])
            sum_fuzzy = addup_unit(row, analysis_indice[1])
            sum_rep100 = addup_unit(row, analysis_indice[2])
            list_sum = [sum_new, sum_fuzzy, sum_rep100]
            lines.append([fname])
            for i in range(len(list_sum)):
                lines.append([templates[var_template.get()][i], list_sum[i]])
            lines.append(['\n'])
    return lines


def calc_html(analysis_read, var_unit, var_template):
    pass


def calc_sum(var_file, var_unit, var_template):
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
    lines = calc_file(analysis_read, var_unit, var_template)
    quote_write.writerows(lines)
    quote.close()

    print('Successfully created:\n' + quote_part_path + '\n' +
          'Click [x] on the tk window and close the program.\n')
