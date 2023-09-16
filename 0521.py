ids =[]
grd =[]
while True:
    s = input().strip()
    if s =='q':
        break
    s = s.split()
    ids.append(s[0])
    grd.append(s[1])
s = input().strip().split()
for i in s:
    if i in ids:
        k = ids.index(i)
        if grd[k]=='F':
            grd[k]='D'
        elif grd[k]=='D':
            grd[k]='D+'
        elif grd[k]=='D+':
            grd[k]='C'
        elif grd[k]=='C':
            grd[k]='C+'
        elif grd[k]=='C+':
            grd[k]='B'
        elif grd[k]=='B':
            grd[k]='B+'
        elif grd[k]=='B+':
            grd[k]='A'
for i in range(len(ids)):
    print(ids[i],grd[i])