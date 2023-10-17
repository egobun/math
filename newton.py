import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def coef(x, y):
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) # return an array of coefficient
def Eval(a, x, r):
    x.astype(float)
    n = len( a ) - 1
    temp = a[n] + (r - x[n])
    for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
    return temp # return the y_value interpolation
'''
def main():
    x = np.array([0,1,2,3])
    y = np.array([0,1,4,9])
    #x = np.array([1910,1920,1930,1940,1950,1960,1970,1980,1990,2000])
    #y = np.array([92228496,106021537,123202624,132164569,151325798,179323175,203211926,226545805,248709873,281421906])
    a = coef(x,y)
    b = Eval(a,x,1.5)

X = [1910,1920,1930,1940,1950,1960,1970,1980,1990,2000]
Y = [92228496,106021537,123202624,132164569,151325798,179323175,203211926,226545805,248709873,281421906]
X1 = np.array([1910,1920,1930,1940,1950,1960,1970,1980,1990,2000])
Y1 = np.array([92228496,106021537,123202624,132164569,151325798,179323175,203211926,226545805,248709873,281421906])
'''
X = [1,2,3,4]
Y = [1,4,9,16]
X1 = np.array([1,2,3,4])
Y1 = np.array([1,4,9,16])
N = len(X)

'''
def fin_diff():
    y = Y.copy()
    for i in range(N - 1):
        for j in range(len(y) - 1):
            y[j] = y[j + 1] - y[j]
        y.pop()
        print(f'd{i + 1}y: {y}')


def div_diff():
    for i, f in zip(range(N - 1), f_gen()):
        print(f'f{i + 1}: {f}')

'''
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
print(Eval(coef(X1,Y1),X1,20))

'''
if __name__ == '__main__':
    print(f'x: {X}')
    print(f'y: {Y}\n')
    print('Finite differences:')
    fin_diff()
    print()
    print('Divided differences:')
    div_diff()
    n_pol = newton()
    print('\nN =', n_pol)
    #print('N4(x1+x2) =', n_pol.subs(symbols('x'), X[1] + X[2]))
    #plot(n_pol, line_color='y')
    #plot(n_pol, xlim=[0, 4], ylim=[0, 10], line_color='y')
    print(Eval(coef(X1,Y1),X,20))
'''