s = input() 
a = [int(i) for i in s]
sm = 0
for i in range(12):
    sm += (13-i)*a[i]
lst = (11-sm%11)%10
print(s[0]+' '+s[1:5]+' '+s[5:10]+' '+s[10:12]+' '+str(lst))