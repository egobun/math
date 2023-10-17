import math
def function1(x):
    return math.sqrt(1-pow(x,2))
def function2(y):
    return math.atan(y)
def solve(x0,y0,R):
    x = x0
    y = y0
    f_x = function2(y0)
    f_y = function1(x0)
    while (abs(x-f_x)>= R and abs(y-f_y) >= R):
        x = f_x
        y = f_y
        f_x = function2(f_y)
        f_y = function1(f_x)
    a = []
    a.append(x)
    a.append(y)
    return a
def main():
    x0 = 0.5
    y0 = 0.5
    R = 0.000001
    answer = solve(x0,y0,R)
    print('x=',answer[0])
    print('y=',answer[1])
    print('x=',-answer[0])
    print('y=',-answer[1])
main()