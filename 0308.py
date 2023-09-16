list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
d=int(input())
m=int(input())
y=int(input())-543
if y%400==0 or ( y%4==0 and y%100!=0):
    list[2]=29
ans = 0
for i in range(1,m):
    ans += list[i]
print(ans+d)