class roman :
    def __init__(self, r):
        s = '0'+r
        nm=0
        for i in range(1,len(s)):
            if s[i] == 'M':nm+=1000
            if s[i] == 'M' and s[i-1] == 'C':nm+=900-1000-100
            if s[i] == 'D':nm+=500
            if s[i] == 'D' and s[i-1] == 'C':nm+=400-500-100
            if s[i] == 'C':nm+=100
            if s[i] == 'C' and s[i-1] == 'X':nm+=90-100-10
            if s[i] == 'L':nm+=50
            if s[i] == 'L' and s[i-1] == 'X':nm+=40-50-10
            if s[i] == 'X':nm+=10
            if s[i] == 'X' and s[i-1] == 'I':nm+=9-10-1
            if s[i] == 'V':nm+=5
            if s[i] == 'V' and s[i-1] == 'I':nm+=4-5-1
            if s[i] == 'I':nm+=1
        self.o = nm%10 #one
        self.t = (nm//10)%10 #tens
        self.h = (nm//100)%10
        self.th = nm//1000
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        o = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        t = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        h = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        return self.th*'M'+h[self.h]+t[self.t]+o[self.o]
    def __int__(self):
        return self.th*1000+self.h*100+self.t*10+self.o
    def __add__(self, rhs):
        vv = int(self)+int(rhs)
        self.o = vv%10 #one
        self.t = (vv//10)%10 #tens
        self.h = (vv//100)%10
        self.th = vv//1000
        return self
t, r1, r2 = input().split() 
a = roman(r1); b = roman(r2) 
if t == '1' : print(a < b) 
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b)) 
else : print(str(a + b))
