from math import pi, sin
class Angle():

    def __init__(self, grad, mnts):
        if (mnts < 0) or (mnts > 60):
            raise ValueError('Введены неверные диапазоны значений. ')
        else:
            self.data = (grad, mnts)

    def read(self, grad, mnts):
        if (mnts < 0) or (mnts > 60):
            raise ValueError('Введены неверные диапазоны значений. ')
        else:
            self.data = (grad, mnts)

    def display(self):
        print("Угол равен", self.data[0], "град.", self.data[1], "мин.")

    def to_string(self):
        return str(self.data[0]) + ', ' + str(self.data[1])

    def to_dec(self, new_grad=-1, new_min=-1):
        if new_grad == -1 or new_min == -1:
            return self.data[0] + self.data[1]/60
        else:
            return new_grad + new_min/60

    def to_grad(self, new_grad=-1, new_min=-1):
        if new_grad == -1 or new_min == -1:
            return self.to_dec() * pi / 180
        else:
            return self.to_dec(new_grad=new_grad, new_min=new_min) * pi / 180

    def change_ang(self, new_grad, new_min, minus=False):
        new_num = self.to_dec(new_grad=new_grad, new_min=new_min)
        if not minus:
            num = self.to_dec() + new_num
        else:
            num = self.to_dec() - new_num
        return self.read(int(num // 1), round(num % 1 * 60))

    def ang_sin(self):
        return sin(self.to_grad())
    
    def ang_eval(self, new_grad, new_min):
        diff = self.to_grad() - self.to_grad(new_grad=new_grad, new_min=new_min)
        if diff == 0:
            print('Углы равны.')
        elif diff < 0:
            print("Угол", str(new_grad) + ", " + str(new_min), "больше угла", self.to_string(), "на", str(abs(diff)), "радиан.")
        else:
            print("Угол", str(new_grad) + ", " + str(new_min), "меньше угла", self.to_string(), "на", str(abs(diff)), "радиан.")
        return diff
