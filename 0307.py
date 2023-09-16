pp = input()
a = len(pp)
if a <= 3 :
    print(pp)
elif a == 4 :
    print(str((int(pp)+50)/1000)[0:3]+'K')
elif a == 5:
    print(str((int(pp)+500)//1000)+'K')
elif a == 6 :
    print(str((int(pp)+500)//1000)+'K')
elif a == 7 :
    print(str((int(pp)+50000)/1000000)[0:3]+'M')
elif a == 8:
    print(str((int(pp)+500000)//1000000)+'M')
elif a == 9 :
    print(str((int(pp)+500000)//1000000)+'M')
elif a == 10 :
    print(str((int(pp)+50000000)/1000000000)[0:3]+'B')
else :
    print(str((int(pp)+500000000)//1000000000)+'B')
