import math

n = float(input())
ans1 = (2*math.pi)**0.5*n**(n+0.5)*math.e**(-n+1/(12*n+1))
ans2 = (2*math.pi)**0.5*n**(n+0.5)*math.e**(-n+1/(12*n))
print(ans1)
print(ans2)