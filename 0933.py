def add_poly(p1, p2):
    p = p1+p2
    ans = []
    d = []
    for i in range(len(p)):
        sumprasit = p[i][0]
        degree = p[i][1]
        if degree in d:continue
        d.append(degree)
        for j in range(len(p)):
            if i == j :continue
            if degree == p[j][1]:
                sumprasit += p[j][0]
        if sumprasit != 0:
            ans.append((degree,sumprasit))
    ans.sort(reverse=True)
    final_ans = [(i[1],i[0]) for i in ans]
    return final_ans
def mult_poly(p1, p2):
    p = []
    for i in p1:
        for j in p2:
            p.append((i[0]*j[0],i[1]+j[1]))
    return add_poly(p,[])
for i in range(3):
    exec(input().strip())