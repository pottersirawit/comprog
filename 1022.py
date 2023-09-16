import numpy as np
def mult_table(nrows, ncols):
 # คืนอาเรย์ที่มี shape เป็น (nrow, ncols) ภายในเก็บตารางสูตรคูณ (ดูตัวอย่างข ้างล่าง)
    A = np.arange(1,nrows+1)
    A = A.reshape((nrows,1))
    B = np.arange(1,ncols+1)
    B = B.reshape((1,ncols))
    return A*B
exec(input().strip()) # ตอ้ งมคี าสงั่ นี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ