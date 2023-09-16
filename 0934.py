def pattern1(nrows, ncols):
    ans = [[0 for j in range(ncols)]for i in range(nrows)]
    k=1
    for i in range(nrows):
        for j in range(ncols):
            ans[i][j]=k
            k+=1
    return ans
def pattern2(nrows, ncols):
    ans = [[0 for j in range(ncols)]for i in range(nrows)]
    k=1
    for i in range(ncols):
        for j in range(nrows):
            ans[j][i]=k
            k+=1
    return ans
def pattern3( N ): # N  0
    ans = [[0 for j in range(N)]for i in range(N)]
    k=1
    for i in range(N):
        for j in range(i,N):
            ans[i][j]=k
            k+=1
    return ans
def pattern4( N ): # N  0
    ans = [[0 for j in range(N)]for i in range(N)]
    k=1
    for i in range(N):
        for j in range(i,-1,-1):
            ans[j][i]=k
            k+=1
    return ans
def pattern5( N ): # N  0
    ans = [[0 for j in range(N)]for i in range(N)]
    k=1
    for y in range(N):
        for x in range(N-y):
            ans[x][y+x]=k
            k+=1
    return ans
def pattern6( N ): # N  0
    ans = [[0 for j in range(N)]for i in range(N)]
    k=1
    for y in range(N):
        if y%2==0:
            for x in range(N-y):
                ans[x][y+x]=k
                k+=1
        else:
            k+=N-y-1
            for x in range(N-y):
                ans[x][y+x]=k
                k-=1
            k+=N-y+1
    return ans
exec(input().strip())