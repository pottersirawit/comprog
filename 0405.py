chk = input()
s = input()
ss =''
ans=0
for i in s:
    if i in ',\'".()':
        ss+=' '
    else:
        ss+=i
ss=ss.split()
for i in ss:
    if i == chk:
        ans+=1
print(ans)