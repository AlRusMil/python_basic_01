"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
* число см толщины полотна.

Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length: int, width: int):
        """

        :param length: протяженность полотна (в м)
        :param width: ширина полотна (в м)
        """
        self._length = length
        self._width = width

    def asphalt_mass_calculation(self, specific_gravity_per_unit: int, blade_thickness: int) -> str:
        """
        Метод расчета массы асфальта, необходимого для покрытия дорожного полотна.
        :param specific_gravity_per_unit: масса асфальта для покрытия одного кв метра дороги,
                                          толщиной 1 см (в кг)
        :param blade_thickness: толщина покрытия (в см)
        :return: какая масса асфальта требуется (либо в кг, либо в т)
        """
        result = self._length * self._width * specific_gravity_per_unit * blade_thickness
        if result > 1000:
            result = f'{int(result / 1000)} т'
        else:
            result = f'{result} кг'
        return result


road_length = 5000
road_weight = 20

per_unit = 25
thickness = 5

my_road = Road(road_length, road_weight)
print("Требуемая масса асфальта: ", my_road.asphalt_mass_calculation(per_unit, thickness))
