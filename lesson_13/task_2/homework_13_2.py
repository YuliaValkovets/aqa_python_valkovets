# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл
# json__<your_second_name>.log

import json
import logging

logging.basicConfig(filename='json_Valkovets.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def read_json_file(json_filename):
    try:
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
    except json.JSONDecodeError as error:
        logger.error(f'Json decode error in file {json_filename}: {error}')
        print(f'Decode error in {json_filename}.The issue has been logged to json_Valkovets.log.')

json_file = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']
for file in json_file:
    read_json_file(file)

