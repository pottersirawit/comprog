import sys
n = int(input())
if n == 0:
    print(0)
    print(0)
    sys.exit()
s1 = set(input().split())
s2 = s1
for i in range(n-1):
    s3 = set(input().split())
    s1 = s1 | s3
    s2 = s2 & s3
print(len(s1))
print(len(s2))