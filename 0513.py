a = []
k = 0
N = int(input())
for i in range(N):
    num=int(input())
    if k%2==0:
        a.append(num)
        k+=1
    else :
        a.insert(0,num)
        k+=1
s = input().strip().split()
for i in range(len(s)):
    if k%2==0:
        a.append(int(s[i]))
        k+=1
    else :
        a.insert(0,int(s[i]))
        k+=1
while True:
    num=int(input())
    if num ==-1 :
        break
    if k%2==0:
        a.append(num)
        k+=1
    else :
        a.insert(0,num)
        k+=1
print(a)