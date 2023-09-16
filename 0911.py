def factor(N):
    ans = []
    md = 2
    while N!=1:
        cnt = 0
        while N%md==0 and N!=1:
            N//=md
            cnt += 1
        if cnt != 0 : ans.append([md,cnt])
        md+=1
    return ans
exec(input().strip())
