chk = input()
if chk ==  'str2RLE':
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
elif chk == 'RLE2str':
    s = input().split()
    for i in range(0,len(s),2):
        print(s[i]*int(s[i+1]),end='')
else:
    print('Error')