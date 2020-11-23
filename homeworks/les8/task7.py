"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:

    @staticmethod
    def is_number(param: str) -> bool:
        try:
            float(param)
            return True
        except ValueError:
            return False

    def __init__(self, real_part: float = 0, complex_part: float = 0):
        self.__real_part = real_part
        self.__complex_part = complex_part

    @property
    def real_part(self):
        return self.__real_part

    @property
    def complex_part(self):
        return self.__complex_part

    def __str__(self):
        result = ('0', str(self.real_part))[self.real_part != 0]
        if self.complex_part > 0:
            result += f' + {self.complex_part}i'
        elif self.complex_part < 0:
            result += f' - {self.complex_part * -1}i'
        else:
            return result
        return result

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real_part + other.real_part,
                                 self.complex_part + other.complex_part)
        elif ComplexNumber.is_number(other):
            return ComplexNumber(self.real_part + other, self.complex_part)
        else:
            raise TypeError("Attempt to add wrong data.\n")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            # (a1a2−b1b2)+(a1b2+b1a2)i
            real_part = self.real_part * other.real_part - self.complex_part * other.complex_part
            complex_part = self.real_part * other.complex_part + self.complex_part * other.real_part
            return ComplexNumber(real_part, complex_part)
        elif ComplexNumber.is_number(other):
            return ComplexNumber(self.real_part * other, 0)
        else:
            raise TypeError("Attempt to multiply wrong data.\n")


complex_number1 = ComplexNumber(5, 7)
complex_number2 = ComplexNumber(3, 9)
complex_number3 = ComplexNumber(4, -5)
complex_number4 = ComplexNumber(-3, 8)

print('complex_number1: ', complex_number1)
print('complex_number2: ', complex_number2)
print('complex_number3: ', complex_number3)
print('complex_number4: ', complex_number4)

try:
    complex_number = complex_number1 + 'a'
except TypeError as te:
    print('1: ', te)

try:
    complex_number = complex_number1 * 'a'
except TypeError as te:
    print('2: ', te)

print('\nAddition')
print('3: ', complex_number1 + 5)
print('4: ', complex_number1 + complex_number2)
print('5: ', complex_number3 + complex_number4)
print('\nMultiplication')
print('6: ', complex_number2 * 5)
print('7: ', complex_number1 * complex_number2)
print('8: ', complex_number2 * complex_number3)

