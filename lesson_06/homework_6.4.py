# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

list_1 = [1, 2, 6, 4, 25, 60, 91, 101, 200, 18]
list_with_even_num = [i for i in list_1 if i % 2 == 0]
print(sum(list_with_even_num))


