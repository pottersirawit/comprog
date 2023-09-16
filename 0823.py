d = {}
for i in range(int(input())):
    s = input().strip().split()
    d[s[0]+' '+s[1]] = s[2]
    d[s[2]] = s[0]+' '+s[1]
for i in range(int(input())):
    s = input()
    if s in d:print(s,'-->',d[s])
    else:print(s,'-->','Not found')