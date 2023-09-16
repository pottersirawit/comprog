import math
a = float(input())
L = 0
U = 0
b = a
while b > 0 :
    b//=10
    U+=1
while True:
    x = (L+U) / 2
    if abs(a - 10**x) <= 10**(-10)*max(a,10**x):
        print(round(x,6))
        break
    elif 10**x > a :
        U=x
    elif 10**x < a :
        L=x 