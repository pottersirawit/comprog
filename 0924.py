d = {}
nm = []
while True:
    s = input()
    if s =='q':
        break
    name,type = s.split(', ')
    if type in nm:
        d[type].append(name)
    else:
        nm.append(type)
        d[type] = [name]
for i in nm:
    print(i+': '+', '.join(d[i]))