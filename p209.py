n = int(input())
l = []
for i in range(n):
    l.append(input().split())
c = input().split()
if c[0] == 'show':
    for i in l:
        print(' '.join(i))
elif c[0] == 'get':
    chk = True
    for i in l:
        if i[0] == c[1]:
             print(' '.join(i))
             chk = False
    if chk:print(c[1],'not found')
elif c[0] == 'avg':
    sm = 0
    for i in l:
        sm += float(i[int(c[1])])
    print(round(sm/n,4))
elif c[0] == 'max':
    mx = -999
    ans = ''
    for i in l:
        if float(i[int(c[1])]) > mx:
            mx = float(i[int(c[1])])
            ans = i[0]
        elif float(i[int(c[1])]) == mx:
            ans = min(ans,i[0])
    print(ans,mx)
elif c[0] == 'sort':
    ls = []
    for i in l:
        ls.append([float(i[int(c[1])]),i[0]])
    ls.sort()
    for i in ls:
        print(i[1],end=' ')