file_name,y = input().strip().split()
sc = []
fn = open(file_name,'r')
for line in fn:
    sid,score = line.split()
    if y[-2:] == sid[0:2]:
        sc.append(float(score))
fn.close()
sc.sort()
if len(sc) == 0:
    print('No data')
else :
    sm = 0
    for i in sc: sm+=i
    print(sc[0],sc[-1],sm/len(sc))