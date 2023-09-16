W = int(input())
price = ''
if W <= 100:
    price = 18
elif 100 < W <= 250:
    price = 22
elif 250 < W <= 500:
    price = 28
elif 500 < W <= 1000:
    price = 38
elif 1000 < W <= 2000:
    price = 58
else :
    price = "Reject"
print(price)