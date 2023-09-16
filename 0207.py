s = input()
a1 = int(s[3]+s[10]+s[17]+s[24]+s[31])
a2 = int(s[7]+s[12]+s[17]+s[22]+s[27])
a3 = a1 + a2 + 10000
key = str(a3)[-4:-1]
key2 = (int(key[0])+int(key[1])+int(key[2]))%10 + 1
arr = ['A','B','C','D','E','F','G','H','I','J']
print(key+arr[key2-1])