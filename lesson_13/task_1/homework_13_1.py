# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і
# приберіть їх. Результат запишіть у файл result_<your_second_name>.csv

import csv

set_1 = set()
set_2 = set()

with open('random.csv', newline='', encoding='utf-8') as csvfile_1:
    reader_1 = csv.reader(csvfile_1)
    header = next(reader_1)
    for row in reader_1:
        row_without_empty_values = (k for k in row if len(k) > 0)
        set_1.add(tuple(row_without_empty_values))

with open('random-michaels.csv', newline='', encoding='utf-8') as csvfile_2:
    reader_2 = csv.reader(csvfile_2)
    next(reader_2)
    for row in reader_2:
        row_without_empty_values = (k for k in row if len(k)>0)
        set_2.add(tuple(row_without_empty_values))

set_with_unique_data = set_1.union(set_2)

with open('result_unique_data.csv', 'w', newline='', encoding='utf-8') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(header)
    writer.writerows(set_with_unique_data)




