s = input()
ans = 0
i = 1
k = 0
ch = 0
arr = [0]*20
while i < 10:
    if s[k] == 'X':
        ans += 10
        #
        if s[k+1] !='X':
            ans += int(s[k+1])
        elif s[k+1] =='X':
            ans += 10
        #
        if s[k+2] =='X':
            ans += 10
        elif s[k+2] == '/':
            ans+= 10 - int(s[k+1])
        else :
            ans+=int(s[k+2])
        #
        arr[i] = ans
        ch = 0
        i+=1
        k+=1
    elif s[k] == '/':
        ans += 10 - int(s[k-1])
        if s[k+1] !='X':
            ans += int(s[k+1])
        elif s[k+1] =='X':
            ans += 10
        arr[i] = ans
        ch = 0
        i+=1
        k+=1
    else :
        ans+=int(s[k])
        k+=1
        ch += 1
        if ch == 2:
            ch = 0
            arr[i] = ans
            i+=1
if s[k] == 'X':
    ans+=10
    if s[k+1] =='X':
        ans+=10
        if s[k+2] =='X':
            ans+=10
        else :
            ans+=int(s[k+2])
    else :
        ans += int(s[k+1])
        if s[k+2] == '/':
            ans += 10 - int(s[k+1])
        else :
            ans += int(s[k+2])
else :
    ans += int(s[k])
    if s[k+1] == '/':
        ans += 10 - int(s[k])
        if s[k+2] =='X':
            ans+=10
        else:
            ans+=int(s[k+2])
    else :
        ans += int(s[k+1])
arr[10] = ans
N = int(input())
if 1 <= N <= 10:
    print(arr[N]-arr[N-1])
else:
    print(arr[10])