a = [int(e) for e in input().split()]
b = []
a.sort()
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        b.append([a[i],a[i+1]])
if len(b)==0:
    print(0)
    print(b[0:10])
elif len(b)==1:
    print(2)
    print(b[0])
else :
    c = []
    c.append(b[0][0])
    c.append(b[0][1])
    for i in range(1,len(b)):
        if c[-1] != b[i][0]:
            c.append(b[i][0])
        c.append(b[i][1])
    print(len(c))
    print(c[0:10])