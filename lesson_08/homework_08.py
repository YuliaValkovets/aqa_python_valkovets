# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою.
# Наприклад: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити виняток
# і вивести “Не можу це зробити!” Використовуйте блок try\except, щоб уникнути інших символів,
# окрім чисел у списку. Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”


def sum_all_numbers(item_array):
    try:
        list_with_string = item_array.split(",")
        list_with_numbers = [int(s) for s in list_with_string]
        sum_numbers = sum(list_with_numbers)
        return f"The sum of the numbers in the list {list_with_numbers} is {sum_numbers}"
    except ValueError as ve:
        return f"Can't be done because {ve}"


array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in array:
    print(sum_all_numbers(item))





