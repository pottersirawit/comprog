n = int(input())
ans = [[],[],[],[]]
for i in range(n):
    ans[0].append(input().split())
cmd = input().split()
for i in range(len(cmd)):
    if cmd[i].isalpha():
        if len(cmd[i]) == 1 or cmd[i] == 'Dog':
            for j in ans[i]:
                if j[1] == cmd[i]:
                    ans[i+1].append(j)
        else :
            for j in ans[i]:
                if j[3] == cmd[i]:
                    ans[i+1].append(j)
    else :
        for j in ans[i]:
            if j[2] == cmd[i]:
                 ans[i+1].append(j)
if len(ans[len(cmd)]) == 0:print('Not Found')
for i in sorted(ans[len(cmd)]):
    print(' '.join(i))