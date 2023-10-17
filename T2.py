import math
import matplotlib.pyplot as plt
import numpy as np
#в следующих двух функциях нужно ввести исследуемую функцию и ее производную
#x*math.exp(-1*pow(x,2))
#(1-2*pow(x,2))*math.exp(-1*pow(x,2))

q = np.linspace(0,10,1000)
p = []
for i in range (1000):
    p.append(q[i]*math.exp(-1*pow(q[i],2))-1/(math.sqrt(2)*2))
plt.plot(q,p)
plt.show()
#math.exp(pow(x,2))*1/(math.sqrt(2)*2)
#math.exp(pow(x,2))*2*pow(x,3)*1/(math.sqrt(2)*2)
fmax = 1/(math.sqrt(2)*pow(math.e,0.5))
def function1(x):
    return fmax/(2*pow(math.e,pow(x,2)))
def pr_function1(x):
    return -1*x*fmax/pow(math.e,pow(x,2))
def function2(x):
    return math.sqrt(math.log(x*2/fmax))
def pr_function2(x):
    return 1/(2*x*function2(x))
print("Введи количество нулей")
N = input()
print("Введи a1")
a1 = float(input())
print("Введи b1")
b1 = float(input())

print("Введи a2")
a2 = float(input())
print("Введи b2")
b2 = float(input())
print("Введи R")
R = float(input())

def find1(a1,b1,R):
    if abs(pr_function1(a1)) < 1:    
        x0 = a1
        print("x0=a")
    elif abs(pr_function1(b1)) < 1:
        x0 = b1
        print("x0=b")
    else:
        print("нет сходимости")

    while True: 
        x1 = function1(x0)
        p = abs(x1-x0)
        x0 = x1
        if (abs(p) <= R):
            print("Ноль функции с заданой точностью R на отрезке [a,b]")
            return x1

def find2(a2,b2,R):
    if abs(pr_function2(a2)) < 1:  
        
        x2 = a2
        print("x0=a")
    elif abs(pr_function2(b2)) < 1:
        
        x2 = b2
        print("x0=b")
    else:
        print(abs(pr_function2(a2))) 
        print(abs(pr_function2(b2)))  
        print("нет сходимости")

    while True: 
        x1 = function2(x2)
        p = abs(x1-x2)
        x2 = x1
        if (abs(p) <= R):
            print("Ноль функции с заданой точностью R на отрезке [a,b]")
            #print(x1)
            #break
            return x1

x1 = find1(a1,b1,R)
x2 = find2(a2,b2,R)
print('ширина на полувысоте=', x2-x1)
