def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m
def mult_c(c, A):
    ans = []
    for i in range(len(A)):
        r = []
        for j in range(len(A[i])):
            r.append(A[i][j]*c)
        ans.append(r)
    return ans
def mult(A, B):
    ans = []
    for i in range(len(A)):
        r = []
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s+=A[i][k]*B[k][j]
            r.append(s)
        ans.append(r)
    return ans
exec(input().strip())