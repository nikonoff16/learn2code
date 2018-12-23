"""
9.21. 
Построить параллелограмм по диагоналям d1, d2 и углу между ними X (в градусах).
"""

from PIL import Image, ImageDraw, ImageFont, ImageGrab
from math import sin, cos, acos, sqrt, radians, degrees


first_diag = float(input("Введите размер первой диагонали: "))
second_diag = float(input("Введите размер второй диагонали: "))
agl = float(input("Введите угол между ними в градусах из двух выбрать тот, который меньше или равен 90 градусам: "))

## Костыль, так как не считало правильно это в самой формуле
semi_1_diag = first_diag / 2
semi_2_diag = second_diag / 2

## Рассчет стороны напротив меньшего угла
a_side = (semi_1_diag**2) + (semi_2_diag**2) - (2*semi_1_diag*semi_2_diag*cos(radians(agl)))
a_side = sqrt(a_side)

## Рассчет стороны напротив большего угла
b_side = (semi_1_diag**2) + (semi_2_diag**2) - (2*semi_1_diag*semi_2_diag*cos(radians(180 - agl)))
b_side = sqrt(b_side)

print("Стороны полигона", a_side, b_side)

## Рассчет площади параллелепипеда
parall_square = 0.5 * first_diag * second_diag * sin(radians(agl))

print("Площадь", parall_square)

## рассчет угла альфа (того угла параллелепипеда, который лежит против меньшей диагонали)
if first_diag < second_diag:
    alfa_side = first_diag
    beta_side = second_diag
else:
    alfa_side = second_diag
    beta_side = first_diag

angle_alfa = degrees(acos(((a_side**2) + (b_side**2) - (alfa_side**2)) / (2 * a_side * b_side)))
print(alfa_side, angle_alfa)

## Рассчет высоты - общая площать на одну из сторон
height = parall_square / a_side

print("Высота", height)

## Вычисление аугмента - рассотяния от угла альфа до встречи с высотой по нижней стороне (он нужен для правильного смещения линий
## при рисовании; все предыдущие рассчеты вели именно к этой величине)
augment = height * (sin(radians(90 - angle_alfa)) / sin(radians(angle_alfa)))

print("Augment: ", augment)

if b_side > a_side:
    bottom_line = int(b_side)
    flank_line = int(height)
else:
    bottom_line = int(a_side)
    flank_line = int(height)

img = Image.new('RGB', (bottom_line + int(augment) + 100, flank_line + 100),'White')
draw = ImageDraw.Draw(img)
draw.polygon(
            (50 + augment, 50,
            bottom_line + augment + 50, 50,
            bottom_line + 50, height + 50,
            50, height + 50),
            fill=('Red'), outline=('Black'))
img.show()
