"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.

Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.

Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:

    __color_variants = ['RED', 'YELLOW', 'GREEN']

    def __init__(self, color: str = 'RED'):
        self.__color = color

    def running(self):
        while True:
            print(f'{self.__color}')
            if self.__color == TrafficLight.__color_variants[0]:
                self.__color = TrafficLight.__color_variants[1]
                time.sleep(7)
            elif self.__color == TrafficLight.__color_variants[1]:
                self.__color = TrafficLight.__color_variants[2]
                time.sleep(2)
            elif self.__color == TrafficLight.__color_variants[2]:
                self.__color = TrafficLight.__color_variants[0]
                time.sleep(5)


# Так как в задании не оговорено иное, решил, что прерывание исполнения скрипта следует делать вручную.
tl = TrafficLight()
tl.running()


# Вариант с контролем переключения.
# Для этого требуется закомментировать первый вариант работы светофора.
class TrafficLight2:
    __color_variants = ['RED', 'YELLOW', 'GREEN']
    __color_check = {'RED': 'GREEN', 'YELLOW': 'RED', 'GREEN': 'YELLOW'}

    def __init__(self, color: str = 'RED'):
        self.__prev_color = color

    def running(self, color) -> bool:
        if TrafficLight2.__color_check[color] != self.__prev_color:
            print("Нарушен порядок переключения!")
            return False

        print(f'{color}')
        if color == TrafficLight2.__color_variants[0]:
            self.__prev_color = color
            time.sleep(7)
        elif color == TrafficLight2.__color_variants[1]:
            self.__prev_color = color
            time.sleep(2)
        elif color == TrafficLight2.__color_variants[2]:
            self.__prev_color = color
            time.sleep(5)

        return True


tl2 = TrafficLight2('RED')
print('1')
if not tl2.running('YELLOW'):
    exit(1)
print('2')
if not tl2.running('GREEN'):
    exit(1)
print('3')
if not tl2.running('RED'):
    exit(1)
print('4')
# Последний оператор if должен завершиться ошибкой.
if not tl2.running('GREEN'):
    exit(1)
print('5')
