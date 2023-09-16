def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    N+=1
    while True:
        if is_prime(N):
            return (N)
        N+=1
 
def next_twin_prime(N):
    N+=1
    while True:
        if is_prime(N) and is_prime(N+2):
            return('('+str(N)+', '+str(N+2)+')')
        N+=1
exec(input().strip())