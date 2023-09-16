q = []
t = []
st = 0 #st
cnt = 0 #count q
pp = 0 #people
qn = 0 #q now
tn = 0 #time now
sum = 0
n = int(input())
for k in range (n):
    c = input().split()
    if c[0] == 'reset':
        st = int(c[1])
    elif c[0] == 'new':
        print('ticket',st+cnt)
        q.append(st+cnt)
        t.append(int(c[1]))
        cnt+=1
    elif c[0] == 'next':
        print('call',q[0])
        qn = q[0]
        tn = t[0]
        q.pop(0)
        t.pop(0)
    elif c[0] == 'order':
        print('qtime',qn,int(c[1])-tn)
        pp+=1
        sum+=int(c[1])-tn
    elif c[0] == 'avg_qtime':
        print('avg_qtime',round(sum/pp,4))