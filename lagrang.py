from sympy import *

X = [0,1,2,3]
Y = [0,-2,-20,-72]
N = 4


def w(j):
    result = 1
    x = symbols('x')
    for i in range(N):
        result *= (x - X[i])
    result /= x - X[j]
    return result


def lagrange():
    L = 0
    for j in range(N):
        L += w(j) / w(j).subs(symbols('x'), X[j]) * Y[j]
    return expand(L)


if __name__ == '__main__':
    print(f'x: {X}')
    print(f'y: {Y}\n')
    lag_pol = lagrange()
    print('L4 =', lag_pol)
    #print('L4(x1+x2) =', lag_pol.subs(symbols('x'), X[1] + X[2]))
    #plot(lag_pol, line_color='g')
    #plot(lag_pol, xlim=[0, 4], ylim=[0, 10], line_color='g')