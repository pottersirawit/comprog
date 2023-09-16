class piggybank:
    def __init__(self):
        self.on = 0
        self.tw = 0
        self.fi = 0
        self.te = 0
    def add1(self, n):
        self.on+=n
    def add2(self, n):
        self.tw+=n
    def add5(self, n):
        self.fi+=n
    def add10(self, n):
        self.te+=n
    def __int__(self):
        return 10*self.te+5*self.fi+2*self.tw+self.on
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    def __str__(self):
        return '{1:'+str(self.on)+', '+'2:'+str(self.tw)+', '+'5:'+str(self.fi)+', '+'10:'+str(self.te)+'}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)