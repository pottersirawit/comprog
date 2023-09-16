def is_29(y):
    return (y%400==0) or (y%4==0 and y%100!=0)
########
def chk(t,d,m,y):
    y-=543
    md31 = [1,3,5,7,8,10,12]
    md30 = [4,6,9,11]
    cc = ['E','Q','N','F']
    if y < 2558-543:return 1
    if m < 1 or m > 12:return 2
    if (m in md31 and (d < 1 or d >31)) or (m in md30 and (d < 1 or d >30)):return 3
    if m==2 and (d<1 or d>28) and not is_29(y):return 3
    if m==2 and (d<1 or d>29) and is_29(y):return 3
    if t not in cc:return 4
    return 0
########
def move_day(d,m,y,cm):
    C = {'E':1,'Q':3,'N':7,'F':14}
    y-=543
    dm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_29(y):dm[2]=29
    else :dm[2]=28
    d+=C[cm]
    if d > dm[m]:
        d-=dm[m]
        m+=1
    if m>12:
        m-=12
        y+=1
    return d,m,y+543
########
error_word = ['Invalid year','Invalid month','Invalid date','Invalid delivery type']
error = []
ans = []
while True:
    s = input()
    if s == 'END':break
    id,t,d,m,y = s.strip().split() # ID Type D M Y
    d=int(d);m=int(m);y=int(y)
    key = chk(t,d,m,y)
    if key == 0:
        d,m,y = move_day(d,m,y,t)
        ans.append([y,m,d,id])
    else :
        error.append([id,t,d,m,y,key])
for id,t,d,m,y,A in error:
    print('Error:',id,t,d,m,y,'-->',error_word[A-1])
ans.sort()
for y,m,d,id in ans:
    print(str(id)+': delivered on '+str(d)+'/'+str(m)+'/'+str(y))