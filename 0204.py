a = input()
b = int(input())
if len(a) >= b:
    print(a)
else :
    print('0'*(b-len(a))+a)