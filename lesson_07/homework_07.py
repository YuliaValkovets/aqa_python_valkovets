# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number):
    for multiplier in range(1,10):
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

multiplication_table(5)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a,b):
    return a + b

print(sum_numbers(3,6))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average_number(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)

print(average_number([6, 9, 9, 5, 9]))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(string):
    return string[::-1]

print(reverse_string("Valkovets"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(list_of_words):
    return max(list_of_words, key=len)

print(longest_word(["Jane", "Karolina", "Max"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

def count_title_words(input_text):
    count = 0
    for word in input_text.split():
        if word.istitle():
            count += 1
    return count

input_text = '''The Blue Marble was the first photograph of the whole Earth and the only one ever taken by a human.
        Fifty years on, new images of the Planet reveal visible changes to the surface.'''
print(count_title_words(input_text))

# task 8
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

def sum_even_numbers(list_with_numbers):
    list_with_even_num = [i for i in list_with_numbers if i % 2 == 0]
    return sum(list_with_even_num)

print(sum_even_numbers([1, 2, 6, 4, 25, 60, 91, 101, 200, 18]))

# task 9
'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, 
які присутні в lst1. Данні в лісті можуть бути будь якими'''

def list_only_with_string (input_list):
    lst_with_string = [x for x in input_list if isinstance(x,str)]
    return lst_with_string

input_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(list_only_with_string(input_list))

# task 10
'''Порахувати кількість унікальних символів в строці. Якщо ї більше 10 - вивести в консоль True, 
інакше - False. Строку отримати за допомогою функції input()'''

def unique_characters (input_str):
    unique_char = set(input_str)
    if len(unique_char) > 10:
        return True
    else:
        return False

input_str = input("Please, enter any string: ")
print(unique_characters(input_str))