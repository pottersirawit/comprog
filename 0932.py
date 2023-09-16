def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for i in range(len(L)):
        s = 0
        for j in range(len(L[i])):
            s+=L[i][j]
        if s+e <= 100:
            L[i].append(e)
            return
    L.append([e])
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    mn = 999
    tmp = 0
    for i in range(len(L)):
        s = 0
        for j in range(len(L[i])):
            s+=L[i][j]
        if s+e <= 100 and 100-s-e < mn:
            mn = 100-s-e
            tmp = i
    if mn == 999:L.append([e])
    else:L[tmp].append(e)
def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    ans = []
    for i in D:
        first_fit(ans,i)
    return ans
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    ans = []
    for i in D:
        best_fit(ans,i)
    return ans
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
