s1 = input().lower()
s2 = input().lower()
a = []
b = []
for i in s1:
    if i != ' ':
        a.append(i)
for i in s2:
    if i != ' ':
        b.append(i)
a.sort()
b.sort()
if a==b:
    print('YES')
else :
    print('NO')