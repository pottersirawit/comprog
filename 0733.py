file_name1,file_name2 = input().strip().split()
ans = []
fn = open(file_name1,'r')
while True:
    t = fn.readline()
    if len(t)==0:
        break
    x=t.strip().split()
    if len(x)==2:
        ans.append([ x[0][-2:] , x[0] , x[1]])
fn.close()
fn = open(file_name2,'r')
while True:
    t = fn.readline()
    if len(t)==0:
        break
    x=t.strip().split()
    if len(x)==2:
        ans.append([ x[0][-2:] , x[0] , x[1]])
fn.close()
ans.sort()
for i in ans:
    print(i[1],i[2])