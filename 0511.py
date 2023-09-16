chk = [0]*10
s = input()
ans = ''
for i in s:
    if i in '1234567890':
        chk[int(i)]=1
for i in range(10):
    if chk[i]==0:
        ans+=str(i)+','
if len(ans) == 0:
    print('None')
else :
    print(ans[:-1])