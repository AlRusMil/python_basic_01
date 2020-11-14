"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


# Дополнительная функция для подсчета общего количества требуемой ткани.
def total_tissue_volume(*args):
    result = 0
    for item in args:
        result += item.clothes_tissue
    return result

class Clothes(ABC):

    def __init__(self, name):
        self.__name = name
        self.__tissue = 0

    @property
    def clothes_name(self):
        return self.__name

    @property
    def clothes_tissue(self):
        return self.__tissue

    @clothes_tissue.setter
    def clothes_tissue(self, value):
        self.__tissue = value

    @abstractmethod
    def tissue_consumption(self) -> float:
        pass


class Coat(Clothes):

    def __init__(self, name):
        self.type = 'coat'
        super().__init__(name)

    # Решил округлить до 2 знаков после запятой, чтобы вывод был более "удобочитаемым.
    def tissue_consumption(self, V: int) -> float:
        self.clothes_tissue = round((V / 6.5 + 0.5), 2)
        return self.clothes_tissue


class Costume(Clothes):

    def __init__(self, name):
        self.type = 'costume'
        super().__init__(name)

    def tissue_consumption(self, H: int) -> float:
        self.clothes_tissue = 2 * H + 0.3
        return self.clothes_tissue


coat = Coat('usual coat')
costume = Costume('super costume')

print(coat.clothes_name)
print(costume.clothes_name)

print(coat.tissue_consumption(65))
print(costume.tissue_consumption(6))

print('Общий объем требуемой ткани составляет: ', total_tissue_volume(coat, costume))
