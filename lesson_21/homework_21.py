import logging
from datetime import datetime


def analyze_heartbeat_intervals(file_log, key_words):

    logging.basicConfig(filename='hb_test.log', level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')

    time_objects = []

    with open(file_log, 'r', encoding='utf-8') as f:
        for row in f:
            if key_words in row:
                index = row.find('Timestamp ')
                if index != -1:
                    time_str = row[index + len("Timestamp "): index + len("Timestamp ") + 8]
                    time_obj = datetime.strptime(time_str, '%H:%M:%S')
                    time_objects.append(time_obj)

    for i in range(len(time_objects) - 1):
       first_time = time_objects[i]
       second_time = time_objects[i+1]
       diff = (first_time - second_time).total_seconds()
       if 31 < diff < 33:
           logging.warning(f'The difference between heartbeat timestamps is {diff} seconds: from {second_time.time()} to {first_time.time()}')
       elif diff >= 33:
           logging.error(f'The difference between heartbeat timestamps is {diff} seconds: from {second_time.time()} to {first_time.time()}')


analyze_heartbeat_intervals('hblog.txt', 'Key TSTFEED0300|7E3E|0400')


            















