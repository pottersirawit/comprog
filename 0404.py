s = input()
a = ''
for i in s:
    if i =='(':
        a+='['
    elif i ==')':
        a+=']'
    elif i =='[':
        a+='('
    elif i ==']':
        a+=')'
    else:
        a+=i
print(a)