n = int(input())
d = {}
for i in range(n):
    name , m1 , m2 = input().split(', ')
    if m1 not in d: d[m1]=[]
    if m2 not in d: d[m2]=[]
    d[m1].append(name)
    d[m2].append(name)
for i in input().split(','):
    i = i.strip()
    print(i,'->',end=' ')
    if i in d:
        print(', '.join(d[i]))
    else:
        print('Not found')