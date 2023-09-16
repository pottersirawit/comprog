import math
list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
bd, bm, by, d, m, y = [int(e) for e in input().split()]
t = 0
by-=543
y-=543
if (by%400==0) or (by%4==0 and by%100!=0):
    list[2]=29
t += list[bm] - bd + 1
for i in range (bm+1 , 13):
    t+=list[i]
if (y%400==0) or (y%4==0 and y%100!=0):
    list[2]=29
else :
    list[2]=28
for i in range (1,m):
    t+=list[i]
t += d - 1
t += (y-by-1)*365
x1 = math.sin(2*math.pi*t/23)
x2 = math.sin(2*math.pi*t/28)
x3 = math.sin(2*math.pi*t/33)
print(t,"{:.2f}".format(x1),"{:.2f}".format(x2),"{:.2f}".format(x3))