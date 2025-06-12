# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhombus:
    def __setattr__(self, name, value):

        if name == 'side_a':
            if value <= 0:
                raise ValueError('The length of the side must be greater than 0')

        if name == 'angle_a':
            if value <= 0 or value >= 180:
                raise ValueError('The angle "a" should be between 0 and 180')
            super().__setattr__('angle_b', 180 - value)

        if name == 'angle_b':
            raise AttributeError('The angle "b" should be set automatically')

        super().__setattr__(name,value)

romb = Rhombus()
romb.side_a = 40
romb.angle_a = 54
print(f'Rhombus characteristics:\nside_a={romb.side_a}\nangle_a={romb.angle_a}\n'
      f'angle_b={romb.angle_b}')

