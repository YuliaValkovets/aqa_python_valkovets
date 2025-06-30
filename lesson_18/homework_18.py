import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def gen_even_numbers(N):
    for i in range(0, N + 1, 2):
        yield i

gen_num = gen_even_numbers(11)
print("Sequence of even numbers:", end=" ")
for k in gen_num:
    print(k, end=',')
print('\n')



#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N
def gen_fibonachi(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a,b = b, a + b

print("Sequence Fibonachi:", end=' ')
gen_fib = gen_fibonachi(37)
for n in gen_fib:
    print(n, end=',')
print('\n')


#Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseList:

    def __init__(self, list_data):
        self.list_data = list_data

    def __iter__(self):
        self.index_last_elem = len(self.list_data) - 1
        return self

    def __next__(self):
        if self.index_last_elem >= 0:
            elem = self.list_data[self.index_last_elem]
            self.index_last_elem -= 1
            return elem
        else:
            raise StopIteration

data = ReverseList(['a', 'b', 'c', 'd'])
new_list = []
for i in data:
    new_list.append(i)
print(f"The items in the list are displayed in reverse order: {new_list}\n")



#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumbers:

    def __init__(self, limit_num):
        self.limit_num = limit_num
        self.start_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_num < self.limit_num:
            num = self.start_num
            self.start_num += 2
            return num
        else:
            raise StopIteration

input_data = EvenNumbers(9)
print("Even numbers:", end=" ")
for k in input_data:
    print(k, end=",")
print('\n')

#Напишіть декоратор, який логує аргументи та результати викликаної функції.
def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} with arguments {args} and {kwargs} was executed with result {result}")
        return result
    return wrapper


#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in function {func.__name__} was occured with error: {e}")
            return None
    return wrapper