order = input().strip()
N = int(input())
s = []
for i in range(N):
    s.append(input().strip())
chk = True
for i in range(N-1):
    if len(s[i])!=len(s[i+1]):
        chk = False
if not chk:
    print('Invalid size')
else :
    if order == 'flip':
        for i in range(N):
            print(s[i][::-1])
    elif order == '90':
        for i in range(len(s[0])):
            for j in range(N-1,-1,-1):
                print(s[j][i],end='')
            print()
    elif order =='180':
        for i in range(N-1,-1,-1):
            print(s[i][::-1])