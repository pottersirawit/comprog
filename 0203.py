month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
d,m,y = input().split('/')
print(month[int(m)-1],d+', '+y)