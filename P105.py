sp = 0
ss = 0
fx = 0
for i in range(9):
    a,b,c = [int(e) for e in input().strip().split()]
    sp+=a
    ss+=b
    if c==1:
        fx+=min(a+2,b)
x = ((1.5*fx -sp)*0.8)
if x < 0:
    x-=1
x = int(x)
print(ss)
print(x)
print(ss-x)