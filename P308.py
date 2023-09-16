N = int(input())
obj = {}
pp = {}
for i in range(N):
    cmd = input().split()
    name = cmd[1]
    thing = cmd[2]
    pp[name] = []
    if cmd[0] == 'B':
        if thing not in obj:
            obj[thing] = []
        chk = True
        for j in range(len(obj[thing])):
            if obj[thing][j][2] == name:
                obj[thing][j] = (-int(cmd[3]),i,name)
                chk = False
        if chk:
            obj[cmd[2]].append((-int(cmd[3]),i,cmd[1])) #ราคา ลำดับ ผู้ประมูล
    elif cmd[0] == 'W':
        for j in range(len(obj[thing])):
            if obj[thing][j][2] == name:
                obj[thing].pop(j)
                break
for thing in obj:
    l = sorted(obj[thing])
    if len(l)!=0:
        wn = l[0][2]
        price = l[0][0]
        pp[wn].append((thing,-price))
for key in sorted(pp):
    print(key+': $',end='')
    price = 0
    for i in pp[key]:
        price += i[1]
    print(price,end='')
    if price != 0:
        print(' -> ',end='')
        for i in sorted(pp[key]):
            print(i[0],end=' ')
    print()