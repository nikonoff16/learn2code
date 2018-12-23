'''
Найти значение переменной z, заданной суммой функций:    
z = f(sinb,a) + f(cosb,a) + f(sin b,а-1) + f(sinb-cosb,a*a-1) + f(sinb*sinb-1,cosа+a), 
где f(u,t) =  u + sin t, если u > 0; u + t если u <= 0 
'''
from math import sin, cos

a = float(input("Введите первую перменную: "))
b = float(input("Введите вторую переменную: "))

def f_func(u_arg, t_arg):
    if u_arg > 0:
        return u_arg + sin(t_arg)
    else:
        return u_arg + t_arg

# print(f_func(a, b))

z_res = f_func(sin(b), a) + f_func(cos(b), a) + f_func(sin(b), a - 1) + f_func(sin(b) - cos(b), a*a - 1) + (f_func(sin(b)*sin(b) - 1, cos(a) + a))

print(z_res)