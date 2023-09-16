def convex_polygon_area(p):
    p.append(p[0])
    n = len(p)
    s1 = 0
    s2 = 0
    for i in range(n):
        s1+=p[i%n][0]*p[(i+1)%n][1]
    for i in range(n):
        s2+=p[i%n][1]*p[(i+1)%n][0]
    return abs((s1-s2)/2)
def is_heterogram(s):
    d = {}
    for i in s.lower():
        if i not in 'abcdefghijklmnopqrstuvwxyz':continue
        if i in d:
            return False
        d[i] = 'eiei'
    return True
def replace_ignorecase(s, a, b):
    ans = ''
    i = 0
    while i < len(s)-len(a)+1:
        if s[i:i+len(a)].lower() == a.lower():
            ans+=b
            i+=len(a)
        else :
            ans+=s[i]
            i+=1
    while i < len(s):
        ans+=s[i]
        i+=1
    return ans
def top3(votes):
    d = []
    for i in votes:
        d.append((-votes[i],i))
    d.sort()
    ans = []
    for i in range(min(3,len(d))):
        ans.append(d[i][1])
    return ans
for k in range(2):
    exec(input().strip())