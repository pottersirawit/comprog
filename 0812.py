d = {}
n = int(input())
for i in range (n):
    nickname,name = input().strip().split()
    d[nickname]=name
    d[name]=nickname
n = int(input())
for i in range (n):
    s = input()
    if s in d:
        print(d[s])
    else:
        print('Not found')