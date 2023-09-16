price = {}
n = int(input())
for i in range(n):
    a,b = input().split()
    b = float(b)
    price[a]=b
n = int(input())
sum = 0
sale = {}
for i in range(n):
    a,b = input().split()
    b = int(b)
    if a not in price: continue
    sum += b*price[a]
    if a in sale:
        sale[a] += b*price[a]
    else :
        sale[a] = b*price[a]
ans = []
mx = 0
for i in sale:
    if sale[i] > mx:
        ans = [i]
        mx = sale[i]
    elif sale[i] == mx:
        ans.append(i)
ans.sort()
if sum == 0:
    print('No ice cream sales')
else :
    print('Total ice cream sales:',sum)
    print('Top sales:',', '.join(ans))