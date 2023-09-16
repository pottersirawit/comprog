S = 'abcdefghijklmnopqrstuvwxyz'
E1 = input().strip()
s1 = ''
for i in E1.lower():
    if i in S:s1+=i
E2 = input().strip()
s2 = ''
for i in E2.lower():
    if i in S:s2+=i
d1 = {}
d2 = {}
ans1 = []
ans2 = []
for i in S:
    d1[i]=0
    d2[i]=0
for i in s1:d1[i]+=1
for i in s2:d2[i]+=1
for i in S:
    if d1[i]==d2[i]:continue
    elif d1[i]>d2[i]:
        ans1.append((i,d1[i]-d2[i]))
    else :
        ans2.append((i,d2[i]-d1[i]))
print(E1)
if len(ans1) == 0:
    print(' - None')
else :
    for i in ans1:
        eiei=''
        if i[1]>1:eiei="'s"
        print(' - remove',i[1],i[0]+eiei)
print(E2)
if len(ans2) == 0:
    print(' - None')
else :
    for i in ans2:
        eiei=''
        if i[1]>1:eiei="'s"
        print(' - remove',i[1],i[0]+eiei)