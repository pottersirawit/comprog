import sys
n = int(input())
k = int(input())
if n < 1 and k < 1:
    print('Invalid n and k')
    sys.exit()
elif n < 1:
    print('Invalid n')
    sys.exit()
elif k < 1:
    print('Invalid k')
    sys.exit()
out = ''
for i in range(1,k+1):
    m = n+1
    if i == k: m = n
    out += str(i)+ '-'*(m-len(str(i)))
print(out)
s = ['0','1']
for i in range(n-1):
    s += s[::-1]
    for i in range(len(s)//2):
        s[i] = '0'+s[i]
    for i in range(len(s)//2,len(s)):
        s[i] = '1'+s[i]
for i in range(2**n):
    if i%k == k-1:
        print(s[i])
    elif i != 2**n-1:
        print(s[i]+',',end='')
    else:
        print(s[i])