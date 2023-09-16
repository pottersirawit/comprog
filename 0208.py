import math
s = input().split(',')
a1 = int(s[0]) #เศษ
a2 = 1 #ส่วน
if s[1] != '':
    b1 = int(s[1]) #เศษ
else :
    b1 = 0
b2 = int('1'+len(s[1])*'0') #ส่วน
c1 = int(s[2])
c2 = int('9'*len(s[2])+'0'*(len(s[1])))
d2 = a2*b2//math.gcd(a2,b2) #LCM
d1 = a1*d2//a2 + b1*d2//b2
e2 = d2*c2//math.gcd(d2,c2)
e1 = d1*e2//d2 + c1*e2//c2
e3 = math.gcd(e1,e2)
print(str(e1//e3)+' / '+str(e2//e3))