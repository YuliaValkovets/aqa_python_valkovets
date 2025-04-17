# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402 # km2
azov_sea_area = 37800 # km2

total_area = black_sea_area + azov_sea_area
print(f"Total area: {total_area} km2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
goods_on_all_warehouses = 375291
goods_on_warehouses_1_2 = 250449
goods_on_warehouses_2_3 = 222950

goods_on_warehouse_1 = goods_on_all_warehouses - goods_on_warehouses_2_3
goods_on_warehouse_3 = goods_on_all_warehouses - goods_on_warehouses_1_2
goods_on_warehouse_2 = goods_on_all_warehouses - goods_on_warehouse_1 - goods_on_warehouse_3
print(f"In the first warehouse: {goods_on_warehouse_1} goods\n"
      f"In the second warehouse: {goods_on_warehouse_2} goods\n"
      f"In the third warehouse: {goods_on_warehouse_3} goods")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months = 18 # 1.5 year
payment_for_month = 1179 # UAH

total_price = months * payment_for_month
print(f"Total price of the computer: {total_price} UAH")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"Remainder from division of numbers:\n"
      f"'8019 % 8' - {a}\n"
      f"'9907 % 9' - {b}\n"
      f"'2789 % 5' - {c}\n"
      f"'7248 % 6' - {d}\n"
      f"'7128 % 5' - {e}\n"
      f"'19224 % 9' - {f}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

count_pizza_large = 4
count_pizza_medium = 2
count_juice = 4
count_cake = 1
count_water = 3
cost_pizza_large = 274 # UAH
cost_pizza_medium = 218 # UAH
cost_juice = 35 # UAH
cost_cake = 350 # UAH
cost_water = 21 # UAH

total_amount_of_money = (cost_pizza_large * count_pizza_large + cost_pizza_medium * count_pizza_medium +
                         cost_juice * count_juice + cost_cake * count_cake + cost_water * count_water)
print(f"Total amount of money for the order: {total_amount_of_money} UAH")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
all_photos = 232
photos_page = 8

pages_needed = all_photos // photos_page
print(f"Ihor needs {pages_needed} pages for all his photos")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600 # km
fuel_100km = 9 # liters
capacity_of_fuel_tank = 48 # liters

total_fuel_for_trip = (distance / 100) * fuel_100km
fuel_station = total_fuel_for_trip // 48
print(f"To travel from Kharkov to Budapest the family will need: {total_fuel_for_trip} liters of fuel.\n"
      f"The family needs to stop at a fuel station: {int(fuel_station)} times")