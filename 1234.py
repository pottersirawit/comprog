class piggybank:
    def __init__(self):
        self.coins = {}
    def add(self, v, n):
        cnt = 0
        for i in self.coins:
            cnt+=self.coins[i]
        if cnt + n >100:
            return False
        v=float(v)
        if v not in self.coins: self.coins[v]=0
        self.coins[v]+=n
        return True
    def __float__(self):
        sm = 0.0
        for i in self.coins:
            sm+=i*self.coins[i]
        return sm
    def __str__(self):
        s = ', '.join([str(i) + ':' + str(self.coins[i]) for i in sorted(self.coins)])
        return '{' + s + '}'
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)