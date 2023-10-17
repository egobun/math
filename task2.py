import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
#в первой функции нужно ввести интегрируемую функцию
#sin(100*x)*math.exp(-pow(x,2))*cos(2*x)
def function(x):
    return sin(100*x)*math.exp(-pow(x,2))*cos(2*x)
print("Введи начало отрезка интегрирования - a")
a = float(input())
print("Введи начало отрезка интегрирования - b")
b = float(input())
print("Введи количество точек разбиения отрезка интегрирования - N")
N = int(input())
def small_integral(N):
    integral = 0
    x_arr = np.linspace(a,b,N)
    delta_x = (b-a)/(N-1)
    for i in range(N-1):
        integral += function(x_arr[i]) * delta_x
    print(integral)
def big_integrall(N):
    integral = 0
    x_arr = np.linspace(a,b,N)
    delta_x = (b-a)/(N-1)
    for i in range(N-1):
        integral += function(x_arr[i+1]) * delta_x
    print(integral)
def middle_integrall(N):
    integral = 0
    x_arr = np.linspace(a,b,N)
    delta_x = (b-a)/(N-1)
    for i in range(N-1):
        integral += function((x_arr[i]+x_arr[i+1])/2) * delta_x
    print(integral)
print("Значение интеграла по левым точкам разбиения")
small_integral(N)
print("Значение интеграла по средним точкам разбиения")
middle_integrall(N)
print("Значение интеграла по правым точкам разбиения")
big_integrall(N)

