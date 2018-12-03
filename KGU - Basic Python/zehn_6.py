'''
10.6 
Создать класс Angle для работы с углами на плоскости, задаваемыми величиной в градусах и минутах. 
Обязательно должны быть реализованы: 
    - перевод в радианы, 
    - приведение к диапазону 0-360, 
    - увеличение и уменьшение угла на заданную величину, 
    - получение синуса, 
    - сравнение углов.
Во всех заданиях, помимо указанных в задании операций, обязательно должны быть реализованы следующие методы:
    - метод инициализации Init;
    - ввод с клавиатуры Read;
    - вывод на экран Display;
    - преобразование в строку toString.

'''

from math import pi, sin
class Angle():

    def __init__(self, grad, mnts):
        if (mnts < 0) or (mnts > 60):
            raise ValueError('Введены неверные диапазоны значений. ')
        else:
            self.data = (grad, mnts)  # Данные хранятся в виде кортежа, где первое число - градусы, второе - минуты

    def read(self, grad, mnts):
        if (mnts < 0) or (mnts > 60):
            raise ValueError('Введены неверные диапазоны значений. ')
        else:
            self.data = (grad, mnts)

    def display(self):
        print("Угол равен", self.data[0], "град.", self.data[1], "мин.")

    def to_string(self):
        return str(self.data[0]) + ', ' + str(self.data[1])

    def to_dec(self, new_grad=-1, new_min=-1):  # перевод числа в десятичную форму
        if new_grad == -1 or new_min == -1:
            return self.data[0] + self.data[1]/60
        else:
            return new_grad + new_min/60

    def to_grad(self, new_grad=-1, new_min=-1):  # перевод градусов в радианы
        if new_grad == -1 or new_min == -1:
            return self.to_dec() * pi / 180
        else:
            return self.to_dec(new_grad=new_grad, new_min=new_min) * pi / 180

    def change_ang(self, new_grad, new_min, minus=False):  # сложение/вычитание углов
        new_num = self.to_dec(new_grad=new_grad, new_min=new_min)
        if not minus:
            num = self.to_dec() + new_num
        else:
            num = self.to_dec() - new_num
        return self.read(int(num // 1), round(num % 1 * 60))  # вызывает метод .read() для записи данных в принятом формате. 
                                                              # изменение сохраняются в инстансе класса

    def ang_sin(self):  # синус угла
        return sin(self.to_grad())
    
    def ang_eval(self, new_grad, new_min):  # сравнение углов. Величины сравниваются в радианах
        diff = self.to_grad() - self.to_grad(new_grad=new_grad, new_min=new_min)
        if diff == 0:
            print('Углы равны.')
        elif diff < 0:
            print("Угол", str(new_grad) + ", " + str(new_min), "больше угла", self.to_string(), "на", str(abs(diff)), "радиан.")
        else:
            print("Угол", str(new_grad) + ", " + str(new_min), "меньше угла", self.to_string(), "на", str(abs(diff)), "радиан.")
        return diff
