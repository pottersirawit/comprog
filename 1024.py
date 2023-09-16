import numpy as np
def peak_indexes(x):
 # x เป็นอาเรย์เก็บจ านวนต่าง ๆ
 # คืนอาเรย์ที่เก็บต าแหน่งใน x ที่เป็น "ยอด"
    ans = np.arange(x.shape[0])
    x1 = np.insert(x,0,999999999)
    x2 = np.append(x,9999999999)
    x1 = np.delete(x1,-1)
    x2 = np.delete(x2,0)
    return ans[( x1 < x ) & (x2 < x)]
def main():
 d = np.array([float(e) for e in input().split()])
 pos = peak_indexes(np.array(d))
 if len(pos) > 0:
    print(", ".join([str(e) for e in pos]))
 else:
    print("No peaks")
exec(input().strip()) # Don't remove this line
