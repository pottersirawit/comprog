d = {'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7,'X':0}
p = [0,0]
while True:
    s = input().strip()
    player = int(s[0])
    for i in range(1,len(s)):p[player-1]+=d[s[i]]
    if s[1]=='K':break
print(p[0],p[1])
if p[0]==p[1] :print('Tie')
elif p[0]>p[1]:print('Player 1 wins')
else:print('Player 2 wins')