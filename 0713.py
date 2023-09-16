s = input()
a = ''
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9' or i == ' ':
        a+=i
    else :
        a+=' '
a=a.split()
print(a[0].lower(),end='')
for i in range (1,len(a)):
    print(a[i][0].upper()+a[i][1:].lower(),end='')