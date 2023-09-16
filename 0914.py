fn1 = input().strip()
fn2 = input().strip()
fn3 = input().strip()
d1 = {}
d2 = {}
fn = open(fn1,'r')
for line in fn:
    d1[line.split(',')[0]]=line.split(',')[1].strip()
fn.close()
fn = open(fn2,'r')
for line in fn:
    d2[line.split(',')[0]]=line.split(',')[1].strip()
fn.close()
fn = open(fn3,'r')
for line in fn:
    x1,x2 = line.strip().split(',')
    if x1 in d1 and x2 in d2:
        print(d1[x1]+','+d2[x2])
    else:
        print('record error')
fn.close()