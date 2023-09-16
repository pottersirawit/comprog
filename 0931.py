def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    return gcd(gcd(a,b),c) == 1
def primitive_Pythagorean_triples(max_len):
 # คืนลิสต์ ทภี่ ายในเกบ็ ลสิตย์ อ่ ยทมี่ สี มาชกิสามคา่ ของ a, b และ c
 # โดยที่ a  b  c  max_len
 # ลิสต์ย่อยต่าง ๆ ถูกจัดเรียงตามค่า c จากน้อยไปมาก 
 # หากมีค่า c เท่ากัน ให้เรียงตามค่า a เชน่ ถา้ max_len = 65 จะได้
 # [[3, 4, 5], [5, 12, 13], [8, 15, 17], [7, 24, 25], 
 # [20, 21, 29], [12, 35, 37], [9, 40, 41], [28, 45, 53], 
 # [11, 60, 61], [16, 63, 65], [33, 56, 65]]
    triplee = []
    for i in range(2,max_len):
        for j in range(1,i):
                a = i**2 - j **2
                b = 2*i*j
                c = i**2 + j **2
                if c**2 == a**2+b**2 and c <= max_len:
                    bb=[a,b,c]
                    bb.sort()
                    if is_coprime(a,b,c):triplee.append([bb[2],bb[0]]+bb)
    triplee.sort()
    triple = []
    for i in triplee:
        triple.append(i[2:])
    return triple
exec(input().strip()) 