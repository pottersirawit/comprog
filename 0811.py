def reverse(d):
    ans = {}
    for i in d:
        ans[d[i]]=i
    return ans
def keys(d, v):
    ans = []
    for i in d:
        if v == d[i]:
            ans.append(i)
    return ans
exec(input().strip())