import numpy as np
import matplotlib.pyplot as plt
from sympy import *
#функции для вычисления экстраполированного значения численности населения


#функции для построения интерполянта в форме Ньютона
X = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
Y = [92228496,106021537,123202624,132164569,151325798,179323175,203211926,226545805,248709873,281421906]

N = len(X)
def value(X,Y,iks):
    N = len(X)
    mas = [ [0]*N for i in range(N+1) ]
    for i in range(N):
        mas[0][i] = X[i]
        mas[1][i] = Y[i]
    for j in range(N-1):
        for i in range(N-j-1):
            mas[j+2][i] = (mas[j+1][i+1]-mas[j+1][i])/(mas[0][j+1+i]-mas[0][i]) 
    sum = mas[1][0]
    for i in range(N-1):
        help = mas[i+2][0]
        for j in range(i+1):
            help = help*(iks-mas[0][j])
        sum += help
    print('Экстраполированное значение численности населения США в 2023 году = ',int(sum),'чел')
    print('Популяция в США в 2023 году = 331 900 000 чел')
    print('Отношение экстраполированного значения к реальному',int(sum)/331900000)


def f_gen():
    f = Y.copy()
    for i in range(N - 1):
        for j in range(len(f) - 1):
            f[j] = (f[j + 1] - f[j]) / (X[j + 1 + i] - X[j])
        f.pop()
        yield f


def newton():
    n = Y[0]
    for j, f in zip(range(N - 1), f_gen()):
        a = 1
        for k in range(j + 1):
            a *= (symbols('x') - X[k])
        n += f[0] * a
    return expand(n)
n_pol = newton()
print('\nN =', n_pol)
value(X,Y,2023)
