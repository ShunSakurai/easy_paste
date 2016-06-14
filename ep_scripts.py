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
csv_indices_weighted = [[4, 8], [12], [16], [20], [24], [28], [32]]


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

    lines = calc_csv(analysis_read, var_rep100, var_heading)

    quote_file = open(quote_full_path, 'w', encoding='utf-8')
    quote_write = csv.writer(quote_file, delimiter=',', lineterminator='\n')
    quote_write.writerows(lines)
    quote_file.close()

    print('\nSuccessfully created:\n' + quote_part_path + '\n' +
          'Click [x] on the tk window and close the program.')


def calc_weighted(var_file):
    print('started')
    analysis_path = var_file.get()
    dl = detect_delimiter(analysis_path)
    analysis_read = csv.reader(open(analysis_path, encoding='utf-16'), delimiter=dl)
    analysis_divided = analysis_path.rsplit('/', 2)
    weighted_full_path = analysis_divided[0] + '/' + analysis_divided[1] + '/weighted_' + analysis_divided[2]
    weighted_part_path = analysis_divided[1] + '/weighted_' + analysis_divided[2]

    csv_indices = csv_indices_weighted
    lines = []
    lines.append([r'If check 100% match is No, delete values in Repeated and 100%'])
    lines.append(['Chargeable words per day (can be changed) :', 2000, '', '', '', '', ''])
    lines.append(['Item', 'Repeated', '100%', '95-99%', '85-94%', '75-84%', '50-74%', 'No Match', 'Translation time', 'Proofreading time', 'Total time (hours)', 'Chargeable words'])
    translation_time = '=(SUM(OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -5, 2))/100*25+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -3)/100*60+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -2)+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -1))/B$2*8*4/5'
    proof_time = '=(SUM(OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -5, 2))/100*25+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -3)/100*60+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -7)+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -6)+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -2)+OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -1))/B$2*8/5'
    total_time = '=SUM(OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -2, 2))'
    weighted_words = '=OFFSET(INDIRECT(ADDRESS(ROW(), COLUMN())), 0, -1)*B$2/8'

    for row in analysis_read:
        if len(row[0].rsplit('.', 1)) == 1:
            pass
        else:
            fname = [get_fname(row[0])]
            words = [addup_unit(row, csv_indices[i]) for i in range(len(csv_indices))]
            equations = [translation_time, proof_time, total_time, weighted_words]
            lines.append(fname + words + equations)

    weighted_file = open(weighted_full_path, 'w', encoding='utf-8')
    quote_write = csv.writer(weighted_file, delimiter=',', lineterminator='\n')
    quote_write.writerows(lines)
    weighted_file.close()

    print('\nSuccessfully created:\n' + weighted_part_path + '\n' +
          'Click [x] on the tk window and close the program.')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
