import csv


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


def calc_csv(analysis_read, var_unit, content):
    if var_unit.get() == 'word':
        analysis_indice = [[8, 12], [16, 20, 24, 28], [32]]
    elif var_unit.get() == 'char':
        raise ValueError('Trados-compatible CSV file doesn\'t contain characters. Please use the HTML format.')
    for i in analysis_read:
        if len(i[0].rsplit('.', 1)) == 1:
            pass
        else:
            fname = i[0].rsplit('\\', 1)[1]
            unit_sum_rep100 = addup_unit(i, analysis_indice[0])
            unit_sum_fuzzy = addup_unit(i, analysis_indice[1])
            unit_sum_new = addup_unit(i, analysis_indice[2])
            content.append([fname])
            content.append(['Translation - New Words', unit_sum_new])
            content.append(['Translation - Fuzzy Matches', unit_sum_fuzzy])
            content.append(['Translation - Repetitions and 100% Matches', unit_sum_rep100])
            content.append(['\n'])


def calc_html(analysis_read, var_unit, content):
    pass


def calc_sum(var_file, var_unit):
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
    content = []
    calc_file(analysis_read, var_unit, content)
    quote_write.writerows(content)
    quote.close()

    print('Successfully created:\n' + quote_part_path + '\n' +
          'Click [x] on the tk window and close the program.\n')
