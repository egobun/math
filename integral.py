import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
#sin(100*x)*exp**(-x**2)*cos(2*x)
def function(x):
    return sin(100*x)*math.exp(-pow(x,2))*cos(2*x)

def small_integral(N):
    integral = 0
    x_arr = np.linspace(0,3,N)
    delta_x = 3/(N-1)
    for i in range(N-1):
        integral += function(x_arr[i]) * delta_x
    print(integral)
def big_integrall(N):
    integral = 0
    x_arr = np.linspace(0,3,N)
    delta_x = 3/(N-1)
    for i in range(N-1):
        integral += function(x_arr[i+1]) * delta_x
    print(integral)
def middle_integrall(N):
    integral = 0
    x_arr = np.linspace(0,3,N)
    delta_x = 3/(N-1)
    for i in range(N-1):
        integral += function((x_arr[i]+x_arr[i+1])/2) * delta_x
    print(integral)
small_integral(10000)
middle_integrall(4000)
big_integrall(4000)

