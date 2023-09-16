s = input()
if s[-1] =='s' or s[-1] =='x':
    print(s+'es')
elif s[-2:] == 'ch':
    print(s+'es')
elif s[-1] =='y' and s[-2] not in 'aeiou':
    print(s[:-1]+'ies')
else :
    print(s+'s')