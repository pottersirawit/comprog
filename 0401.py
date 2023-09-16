a = input()
avg = 0
cnt = 0
if a =='q':
    print("No Data")
else :
    while a!='q':
        avg+=float(a)
        cnt+=1
        a = input()
    print(round(avg/cnt,2))