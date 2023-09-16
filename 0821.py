d = {}
s = input().lower()
for i in s:
    if i not in 'abcdefghijklmnopqrstuvwxyz':
        continue
    if i in d:
        d[i] += 1
    else :
        d[i] = 1
ans = [[-d[e],e] for e in d]
ans.sort()
for i in ans:
    print(i[1]+' -> '+str(-i[0]))
