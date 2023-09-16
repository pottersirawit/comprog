N = int(input())
ans = []
for i in range(N):
    x,y = [float(e) for e in input().strip().split()]
    ans.append([(x**2+y**2)**0.5,i+1,x,y])
ans.sort()
print('#'+str(ans[2][1])+': ('+str(ans[2][2])+', '+str(ans[2][3])+')')