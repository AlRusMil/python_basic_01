"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def func_wage(work_hours: float, rate: float, prize: float) -> float:
    """
    Employee payroll
    :param work_hours: number of hours worked
    :param rate: hourly pay
    :param prize: performance bonus
    :return: wage
    """
    return (work_hours * rate) + prize


try:
    _, working_hours, rate, prize = argv

    working_hours = float(working_hours)
    rate = float(rate)
    prize = float(prize)

    print("Итоговая заработная плата составляет: ", func_wage(working_hours, rate, prize))
except ValueError:
    print("Недосаточное количество аргументов (должно быть три)! "
          "Или неверный формат аргументов (должны быть числа)!")
