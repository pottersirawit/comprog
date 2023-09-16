def cnt(s,c):
    cnt = 0
    for i in s:
        if c==i:
            cnt+=1
    return cnt
n = int(input())
d = {}
for i in range(n):
    nm = input()
    s = input()
    lw = [i for i in s.split()]
    st = set(lw)
    d[nm] = [lw,len(lw),len(st)]
while(True):
    word = input()
    if word == '-1':
        break
    mx = 0
    c = 'NOT FOUND'
    for i in d:
        aa = 1/d[i][2]*cnt(d[i][0],word)/d[i][1]
        if aa > mx:
            c=i
            mx=aa
    print(c)
