# Завдання 3:
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
# повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def search_elements_in_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        number_group = group.find('number')
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logger.info(f'Group number is {number_group.text} and incoming is {incoming.text}')
            else:
                logger.info(f'Group number is {number_group.text}, incoming Not found')
        else:
            logger.info(f'Group number is {number_group.text}, incoming Not found')

search_elements_in_xml('groups.xml')