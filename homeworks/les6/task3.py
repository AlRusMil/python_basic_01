"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }


class Position(Worker):
    def get_full_name(self) -> str:
        """
        Метод формирует наименование должности и полного имени
        :return: возвращает должность и полное имя
        """
        full_name = f'{self.position} {self.name} {self.surname}'
        return full_name

    def get_total_income(self) -> int:
        """
        Метод формирует доход
        :return: доход сотрудника с учетом оклада и премии
        """
        return self._income["wage"] + self._income["bonus"]


position1 = Position('Ivan', 'Petrov', 'Engineer', 10000, 2500)
position2 = Position('Petr', 'Vasilev', 'Employee', 8000, 1500)

print("Информация по 1 экземпляру")
print("Полное имя: ", position1.get_full_name())
print("Доход: ", position1.get_total_income())
print("Имя: ", position1.name)
print("Фамилия: ", position1.surname)
print("Должность: ", position1.position)
print("Оклад: ", position1._income['wage'])
print("Премия: ", position1._income['bonus'])

print("\nИнформация по 2 экземпляру")
print("Полное имя: ", position2.get_full_name())
print("Доход: ", position2.get_total_income())
print("Имя: ", position2.name)
print("Фамилия: ", position2.surname)
print("Должность: ", position2.position)
print("Оклад: ", position2._income['wage'])
print("Премия: ", position2._income['bonus'])

