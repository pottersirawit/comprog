import numpy as np
def read_data():
 # อ่านข ้อมูลจากแป้นพิมพ์ จากนั้นสร้างและคืนอาเรย์สองตัว
 # weight เป็นอาเรยส์ ามชอ่ งเก็บน ้าหนักของคะแนนกลางภาค ปลายภาค และโครงงาน (float)
 # data เป็นอาเรย์ขนาด n4 เก็บข ้อมูลนักเรียน n คน แต่ละคนมีข ้อมูล
 # เลขประจ าตัว คะแนนกลางภาค ปลายภาค และโครงงาน (int)
 w = [float(e) for e in input().split()]
 weight = np.array(w)
 n = int(input())
 data = np.ndarray((n, 4), int)
 for i in range(n):
    data[i] = [int(e) for e in input().split()]
 return weight, data
 
def report_lower_than_mean(weight, data):
 # แสดงเลขประจ าตัวที่ได ้คะแนนรวมต ่ากว่าคะแนนเฉลี่ย
 # ให ้แสดงบนบรรทัดเดียวกันหมดคั่ นด ้วยเครื่องหมายจุลภาคและชอ่ งวา่ งหนงึ่ ชอ่ ง
 # เรียงตามล าดับที่ปรากฎใน data ถ้าไม่มีใครได ้ต ่ากว่าคะแนนเฉลี่ยเลย ให ้แสดงค าว่า None
    m = np.mean(np.sum(weight*data[:,1:],axis=1))
    ans = []
    for i in data:
        if np.sum(i[1:]*weight) < m:
            ans.append(str(i[0]))
    if len(ans)==0:print('None')
    else:print(', '.join(ans))
exec(input().strip())