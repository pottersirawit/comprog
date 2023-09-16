N = int(input())
pta = 0
ptb = 0
chk = False
for i in range(0,3*N):
    a,b = input().strip().split()
    if a == 'R' and b =='P':
        ptb+=1
    if a == 'R' and b =='S':
        pta+=1
    if a == 'S' and b =='P':
        pta+=1
    if a == 'S' and b =='R':
        ptb+=1
    if a == 'P' and b =='S':
        ptb+=1
    if a == 'P' and b =='R':
        pta+=1
    if pta == N:
        print(pta,ptb)
        print("Player 1 wins")
        chk = True
        break
    elif ptb == N:
        print(pta,ptb)
        print("Player 2 wins")
        chk = True
        break
if not chk:
    print(pta,ptb)
    print('Tie')