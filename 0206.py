u = input()
u = u[1:-1:1]
v = input() 
v = v[1:-1:1]
u = u.split(', ')
v = v.split(', ')
ans = [0.0]*3
for i in range (3):
    u[i]=float(u[i])
    v[i]=float(v[i])
    ans[i]=u[i]+v[i]
print(u,'+',v,'=',ans)