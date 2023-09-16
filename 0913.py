winner = []
d = {}
n = int(input())
for i in range(n):
    s1,s2 = input().split()
    if s1 not in d:
        d[s1] = 1
    else :
        d[s1]+=1
    if s2 not in d:
        d[s2] = -999999
    else :
        d[s2]-=999999
for i in d:
    if d[i] > 0:
        winner.append(i)
print(sorted(winner))