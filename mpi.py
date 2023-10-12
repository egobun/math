import math
#в следующих двух функциях нужно ввести исследуемую функцию и ее производную
def function(x):
    return ((2-3*pow(x,3))/5)
def pr_function(x):
    return ((-9*x**2))/5
print("Введи a")
a = float(input())
print("Введи b")
b = float(input())
print("Введи R")
R = float(input())

if abs(function(a)) < 1:    
    x0 = a
elif abs(function(b)) < 1:
    x0 = b
else:
    print("нет сходимости")

while True: 
    x1 = function(x0)
    p = x1-x0
    x0 = x1
    if (abs(p) < R):
        print("Ноль функции с заданой точностью R на отрезке [a,b]")
        print(x1)
        break


