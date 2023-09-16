def is_odd(n):
    return n%2==1 
def has_odds(x):
    for i in x:
        if i%2==1:return True
    return False
def all_odds(x):
    for i in x:
        if i%2==0:return False
    return True
def no_odds(x):
    for i in x:
        if i%2==1:return False
    return True
def get_odds(x):
    return [i for i in x if i%2==1]
def zip_odds(a, b):
    a1 = [i for i in a if i%2==1]
    a2 = [i for i in b if i%2==1]
    n = max(len(a1),len(a2))
    ans = []
    for i in range(n):
        if i < len(a1):ans.append(a1[i])
        if i < len(a2):ans.append(a2[i])
    return ans
exec(input().strip())
