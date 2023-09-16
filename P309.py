member1 = {}
member2 = {}
member3 = {}
ota = {}
while True:
    s = input().split()
    if s[0] == '1':
        l = [(-member1[key],key) for key in member1]
        l.sort()
        print(l[0][1]+', '+l[1][1]+', '+l[2][1])
        break
    if s[0] == '2':
        l = [(-len(member2[key]),key) for key in member2]
        l.sort()
        print(l[0][1]+', '+l[1][1]+', '+l[2][1])
        break
    if s[0] == '3':
        for key in ota:
            l = [(-ota[key][mem],mem) for mem in ota[key]]
            l.sort()
            member3[l[0][1]] += 1
        l = [(-member3[key],key) for key in member3]
        l.sort()
        print(l[0][1]+', '+l[1][1]+', '+l[2][1])
        break
    otaname = s[0]
    mbname = s[1]
    sc = int(s[2])
    if mbname not in member1:member1[mbname] = 0
    if mbname not in member3:member3[mbname] = 0
    member1[mbname] += sc
    if mbname not in member2:member2[mbname] = set()
    member2[mbname].add(otaname)
    if otaname not in ota:ota[otaname] = {}
    if mbname not in ota[otaname]: ota[otaname][mbname] = 0
    ota[otaname][mbname] += sc