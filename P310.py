import numpy as np
def eq(A,B,p):
    all = 1
    for i in A.shape:
        all*=i
    sm = np.sum(A==B)
    return sm/all*100 >= p
def closest_point_indexes(points, p):
    ar = (points-p)**2
    sm = np.sum(ar,axis=1)
    mn = np.min(sm)
    idx = np.arange(sm.shape[0])
    return idx[sm==mn]
def number_of_inversions(A):
    cnt = 0
    N = A.shape[0]
    for i in range(N):
        cnt += np.sum(A[i]>A[i+1:])
    return cnt
exec(input().strip())