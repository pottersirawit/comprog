d = {'A' : 1,'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9,'T' : 10,'J' :11,'Q' : 12,'K' : 13,'C' : 1,'D':2,'H':3,'S':4}
s = input()
n = len(s)//2
for i in range(n-1):
    if d[s[i*2]]!=d[s[i*2+2]]:
        if d[s[i*2]]-d[s[i*2+2]] > 0:print('+'+str(d[s[i*2]]-d[s[i*2+2]]),end='')
        else: print(d[s[i*2]]-d[s[i*2+2]],end='')
    else:
        if d[s[i*2+1]]-d[s[i*2+3]] > 0:print('+'+str(d[s[i*2+1]]-d[s[i*2+3]]),end='')
        else: print(d[s[i*2+1]]-d[s[i*2+3]],end='')