c = {'January' : 1,'February' : 2,'March' : 3,'April' : 4,'May' : 5,'June' : 6 ,\
     'July' : 7,'August' : 8,'September' : 9,'October' : 10,'November' : 11,'December' : 12}
a = input().strip().split()
b = input().strip().split()
a[2] = int(a[2][:-1])
b[2] = int(b[2][:-1])
a[3] = int(a[3])
b[3] = int(b[3])
if a[3] < b[3]:
    print(a[0])
elif b[3] < a[3]:
    print(b[0])
else :
    if c[a[1]] < c[b[1]]:
        print(a[0])
    elif c[a[1]] > c[b[1]]:
        print(b[0])
    else :
        if a[2] < b[2]:
            print(a[0])
        elif b[2] < a[2]:
            print(b[0]) 
        else:
            print(a[0],b[0])
