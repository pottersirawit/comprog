d = {}
while True:
    s = input().strip().split()
    if len(s) == 1:
        ans = set()
        ans.add(s[0])
        if s[0] in d: 
            for i in d[s[0]]:
                ans.add(i)
                for j in d[i]:
                    ans.add(j)
        ans2 = list(ans)
        ans2.sort()
        for i in ans2:
            print(i)
        break
    else :
        if s[0] in d:
            d[s[0]].add(s[1])
        else :
            d[s[0]] = {s[1]}
        if s[1] in d:
            d[s[1]].add(s[0])
        else :
            d[s[1]] = {s[0]}