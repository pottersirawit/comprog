N = int(input())
min1 = 99999999
max1 = -99999999
min2 = 99999999
max2 = -99999999
for i in range (N):
    a,b=[int(j) for j in input().split()]
    if i % 2 == 0:
        min1 = min(min1,a)
        max1 = max(max1,b)
        min2 = min(min2,b)
        max2 = max(max2,a)
    else :
        min1 = min(min1,b)
        max1 = max(max1,a)
        min2 = min(min2,a)
        max2 = max(max2,b)
chk = input()
if chk == 'Zig-Zag':
    print(min1,max1)
elif chk == 'Zag-Zig':
    print(min2,max2)