card = input().strip().split()
N = len(card)
s = input()
for i in s:
    if i == 'C':
        card = card[N//2:N] + card[0:N//2] 
    elif i == 'S':
        tmp = []
        for j in range(N//2):
            tmp.append(card[j])
            tmp.append(card[j+N//2])
        card = tmp
for i in card:
    print(i,end=' ')