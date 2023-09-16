def distance1(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
 
def distance2(p1, p2):
    return distance1(p1[0],p1[1],p2[0],p2[1])
 
def distance3(c1, c2):
    dis = distance1(c1[0],c1[1],c2[0],c2[1])
    overlap = False
    if dis <= c1[2]+c2[2]:
        overlap = True
    return(dis,overlap)

 
def perimeter(points):
    k = len(points)
    points.append(points[0])
    pt = 0
    for i in range(k):
        pt += distance1(points[i][0],points[i][1],points[i+1][0],points[i+1][1])
    return pt

exec(input().strip())
