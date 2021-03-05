# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:

    def __init__(self):
        self.element = 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Mud()
        else:
            return None

    def __str__(self):
        return self.element


class Air:

    def __init__(self):
        self.element = 'Air'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return other + self
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None


class Fire:

    def __init__(self):
        self.element = 'Fire'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Air):
            return other + self
        elif isinstance(other, Water):
            return other + self
        elif isinstance(other, Ground):
            return Lava()
        else:
            return None


class Ground:

    def __init__(self):
        self.element = 'Ground'

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Air):
            return other + self
        elif isinstance(other, Water):
            return other + self
        elif isinstance(other, Fire):
            return other + self
        else:
            return None



class Storm:

    def __init__(self):
        self.element = 'Storm'

    def __str__(self):
        return self.element


class Mud:

    def __init__(self):
        self.element = 'Mud'

    def __str__(self):
        return self.element


class Lightning:

    def __init__(self):
        self.element = 'Lightning'

    def __str__(self):
        return self.element


class Steam:

    def __init__(self):
        self.element = 'Steam'

    def __str__(self):
        return self.element


class Dust:

    def __init__(self):
        self.element = 'Dust'

    def __str__(self):
        return self.element


class Lava:

    def __init__(self):
        self.element = 'Lava'

    def __str__(self):
        return self.element


first_elem = Fire()
second_elem = Air()
print(f'{first_elem} + {second_elem} = {first_elem + second_elem}')
