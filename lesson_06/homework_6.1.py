# Порахувати кількість унікальних символів в строці. Якщо їх
# більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

user_input = input("Please, enter any string: ")
unique_char = set(user_input)
count_char = len(unique_char)
if count_char > 10:
    print("True")
else:
    print("False")