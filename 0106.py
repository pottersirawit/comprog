h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
if s2>=s1 :
    ds = s2-s1
else :
    ds = 60-s1+s2
    m2-=1
if m2>=m1 :
    dm = m2-m1
else :
    dm = 60-m1+m2
    h2-=1
if h2>=h1 :
    dh = h2-h1
else :
    dh = 24-h1+h2
print(str(dh)+":"+str(dm)+":"+str(ds))