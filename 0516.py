n = int(input())
ans = []
ans.append(n)
while n != 1:
    if n % 2 ==0:
        n=n//2
    else :
        n = 3*n +1
    ans.append(n)
c = ans[-1:-16:-1]
sze = len(c)
print(c[sze-1],end='')
for i in range(sze-2,-1,-1):
    print('->'+str(c[i]),end='')