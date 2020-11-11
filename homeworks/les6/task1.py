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
            if self.__color == TrafficLight.__color_variants[0]:
                print(f'{self.__color}')
                self.__color = TrafficLight.__color_variants[1]
                time.sleep(7)
            elif self.__color == TrafficLight.__color_variants[1]:
                print(f'{self.__color}')
                self.__color = TrafficLight.__color_variants[2]
                time.sleep(2)
            elif self.__color == TrafficLight.__color_variants[2]:
                print(f'{self.__color}')
                self.__color = TrafficLight.__color_variants[0]
                time.sleep(5)


tl = TrafficLight()

tl.running()
