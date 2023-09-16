def total(pocket):
    sum  = 0
    for i in pocket:sum += i*pocket[i]
    return sum
def take(pocket, money_in):
    for i in money_in:
        if i in pocket:pocket[i]+=money_in[i]
        else:pocket[i]=money_in[i]
    return pocket
def pay(pocket, amt):
    pk = []
    for i in pocket:
        pk.append([i,pocket[i]])
    pk.sort(reverse=True)
    ans = {}
    pkcp = {}
    for i in pocket:pkcp[i] = pocket[i]
    #print('pocket=',pkcp)
    for i in pk:
        us = min(amt//i[0],i[1])
        amt -= us*i[0]
        pocket[i[0]] -= us
        if us != 0:
            ans[i[0]] = us
    if amt != 0:
        for i in pocket:pocket[i] = pkcp[i]
        ans = {}
        #print('YESYESYES')
    #print('pocket=',pkcp)
    return ans
exec(input().strip())