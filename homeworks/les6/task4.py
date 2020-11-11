"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


# Добавил комментарии только к дополнительным методам классов!
class Car:
    def __init__(self, name: str, color: str, speed: int, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('А/м поехала.')

    def stop(self):
        print('А/м остновилась.')

    def turn(self, direction: str):
        print(f'А/м повернула {direction}')

    # Решил добавить метод изменения скорости
    def change_speed(self, speed: int):
        """
        Устанавливается новое значение скорости а/м.
        :param speed: новое значение скорости
        """
        self.speed = speed

    def show_speed(self):
        print(f'Текущая скорость автомобиля составляет {self.speed}')


class TownCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.type = 'Town'
        super().__init__(name, color, speed)

    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'Вы превысили допустимый лимит скорости на {self.speed - speed_limit}')
            print(f'Для автомобиля типа "{self.type}" установлен лимит: {speed_limit}')
        else:
            print(f'Текущая скорость автомобиля составляет {self.speed}')


class SportCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.type = 'Sport'
        super().__init__(name, color, speed)

    def more_power(self):
        """
        Издает рев мотора и увеличивает скорость спорткара на 50.
        """
        self.speed += 50
        print("WRUM WRUM WRUM!!!")


class WorkCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.type = 'Work'
        super().__init__(name, color, speed)

    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'Вы превысили допустимый лимит скорости на {self.speed - speed_limit}')
            print(f'Для автомобиля типа "{self.type}" установлен лимит: {speed_limit}')
        else:
            print(f'Текущая скорость автомобиля составляет {self.speed}')


class PoliceCar(Car):
    def __init__(self, name: str, color: str, speed: int):
        self.type = 'Police'
        super().__init__(name, color, speed, True)

    def pursuit(self):
        """
        Звук сирены.
        """
        print("WIU WIU WIU!")


town_car = TownCar("Гранта", "Red", 50)
sport_car = SportCar("Ferrari", "Black", 200)
work_car = WorkCar("Газель", "White", 50)
police_car = PoliceCar("Ford", "blue", 80)

print("Городская машина.")
print("Наименование автомобиля: ", town_car.name)
print("Цвет автомобиля: ", town_car.color)
print("Тип автомобиля: ", town_car.type)
town_car.show_speed()
town_car.change_speed(90)
town_car.show_speed()
print("Полицейская ли машина? ", town_car.is_police)
town_car.go()
print()


print("Спортивная машина.")
print("Наименование автомобиля: ", sport_car.name)
print("Цвет автомобиля: ", sport_car.color)
print("Тип автомобиля: ", sport_car.type)
sport_car.show_speed()
sport_car.more_power()
sport_car.show_speed()
print("Полицейская ли машина? ", sport_car.is_police)
sport_car.go()
sport_car.stop()
print()

print("Служебная машина.")
print("Наименование автомобиля: ", work_car.name)
print("Цвет автомобиля: ", work_car.color)
print("Тип автомобиля: ", work_car.type)
work_car.show_speed()
work_car.change_speed(39)
work_car.show_speed()
print("Полицейская ли машина? ", work_car.is_police)
work_car.go()
work_car.turn('налево')
print()

print("Полицейская машина.")
print("Наименование автомобиля: ", police_car.name)
print("Цвет автомобиля: ", police_car.color)
print("Тип автомобиля: ", police_car.type)
police_car.show_speed()
police_car.pursuit()
print("Полицейская ли машина? ", police_car.is_police)
police_car.go()
police_car.turn('налево')
police_car.turn('направо')
police_car.turn('обратно')
police_car.stop()
