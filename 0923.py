def strtotme(a):
    m,s = a.split(':')
    return int(m)*60+int(s)
def tmetostr(a):
    m = a//60
    s = a-m*60
    m = str(m)
    s = str(s)
    if len(s) == 1:
        s = '0'+s
    return m+':'+s
n = int(input())
d = {}
for i in range(n):
    s = input().split(', ')
    if s[2] not in d:
        d[s[2]] = strtotme(s[3])
    else :
        d[s[2]] += strtotme(s[3])
ans = [[d[i],i] for i in d]
ans.sort(reverse=True)
for i in range(min(len(ans),3)):
    print(ans[i][1],'-->',tmetostr(ans[i][0]))