s = input()
tmp = s[0]
cnt=1
for i in range(1,len(s)):
    if s[i] == tmp:
        cnt+=1
    else :
        print(tmp,cnt,end =' ')
        tmp=s[i]
        cnt=1
print(tmp,cnt)