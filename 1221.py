class Complex :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        s = ''
        if self.a != 0:s+=str(self.a)
        if self.b != 0:
            if self.b == -1:
                return s+'-i'
            if len(s) and self.b > 0: s+='+'
            if abs(self.b) != 1 : s+=str(self.b)
            s+='i'
        if len(s)==0: return '0'
        return s
    def __add__(self, rhs):
        return Complex(self.a+rhs.a,self.b+rhs.b)
    def __mul__(self, rhs):
        return Complex(self.a*rhs.a-self.b*rhs.b,self.a*rhs.b+self.b*rhs.a)
    def __truediv__(self, rhs):
        return Complex((self.a*rhs.a+self.b*rhs.b)/(rhs.a**2+rhs.b**2),(self.b*rhs.a-self.a*rhs.b)/(rhs.a**2+rhs.b**2))

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2) 
else : print(c1/c2)
