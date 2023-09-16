def spiral_square(n): # n is a positive odd number
    ans = [[0 for j in range (n)] for i in range(n)]
    cmd = [(0,-1),(-1,0),(0,1),(1,0)]
    x =  n-1 ; y = n-1 ; nb = n**2 ; z = 0
    while nb > 0:
        #print(x,y,nb)
        ans[x][y] = nb
        nb-=1
        if x+cmd[z%4][0] < 0 or x+cmd[z%4][0] == n:
            z+=1
        if y+cmd[z%4][1] < 0 or y+cmd[z%4][1] == n:
            z+=1
        if ans[x+cmd[z%4][0]][y+cmd[z%4][1]] != 0:
            z+=1
        x+=cmd[z%4][0]
        y+=cmd[z%4][1]
    return ans
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())