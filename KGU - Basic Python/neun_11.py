from PIL import Image, ImageDraw, ImageFont, ImageGrab
from math import sqrt

x = int(input("Введите ширину изображения: "))
y = int(input("Введите высоту изображения: "))
a = int(input("Введите размер стороны квадрата: "))

def drw_trngl_wtn_sqwr(x_set=1920, y_set=1000, a_size=500):  # В значениях по умолчанию - отладочная информация.
    img = Image.new('RGB', (x_set, y_set),'White')
    draw = ImageDraw.Draw(img)
    ## Рисунок ориентируем по центру созданного полотна. 
    # Создаем квадрат
    draw.polygon((x_set/2 - a_size/2, y_set/2 - a_size/2, 
                  x_set/2 + a_size/2, y_set/2 - a_size/2, 
                  x_set/2 + a_size/2, y_set/2 + a_size/2,
                  x_set/2 - a_size/2, y_set/2 + a_size/2),
                  fill=("Red"), outline=("Black"))
    # Создаем равносторонний треугольник
    draw.polygon((x_set/2 - a_size/2, y_set/2 - a_size/2, 
                  x_set/2 + a_size/2, y_set/2 - a_size/2, 
                  x_set/2, y_set/2 - a_size/2 + a_size*sqrt(3)/2),  # Для нахождения верной точки пользуемся формулой нахождения биссектрисы 
                  fill=("Yellow"), outline=("Black"))
    font = ImageFont.truetype('arial.ttf', 35)
    text = "Квадрат со вписанным треугольником со стороной " + str(a_size) + "px."
    draw.text((x_set/2 - len(text)*9, y_set/2 + a_size/2 + 15), text, 'Black', font=font)

    return img.show()

drw_trngl_wtn_sqwr(x, y, a)
# drw_trngl_wtn_sqwr()
              