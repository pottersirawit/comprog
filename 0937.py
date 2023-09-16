n = int(input())
d = {}
for i in range(n):
    s = input().split()
    d[s[0]] = int(s[1])
m = int(input())  
l = []  
for i in range(m):
    s = input().split()
    l.append((float(s[1]),s[2],s[3],s[4],s[5],s[0]))
l.sort(reverse=True)
ans = []
for i in l :
    if d[i[1]]>0:
        d[i[1]]-=1
        ans.append((i[5],i[1]))
    elif d[i[2]]>0:
        d[i[2]]-=1
        ans.append((i[5],i[2]))
    elif d[i[3]]>0:
        d[i[3]]-=1
        ans.append((i[5],i[3]))
    elif d[i[4]]>0:
        d[i[4]]-=1
        ans.append((i[5],i[4]))
ans.sort()
for i in ans:
    print(i[0],i[1])