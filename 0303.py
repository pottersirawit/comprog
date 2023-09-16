sc = input().split()
sc[0]=float(sc[0])
sc[1]=float(sc[1])
sc[2]=float(sc[2])
sc[3]=float(sc[3])
mn = sc[0]
mx = sc[0]
if sc[1] < mn:
    mn = sc[1]
if sc[2] < mn:
    mn = sc[2]
if sc[3] < mn:
    mn = sc[3]
if sc[1] > mx:
    mx = sc[1]
if sc[2] > mx:
    mx = sc[2]
if sc[3] > mx:
    mx = sc[3]
print(round((sc[0]+sc[1]+sc[2]+sc[3]-mn-mx)/2,2))