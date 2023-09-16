def make_int_list(x):
    return [int(e) for e in x.split()]
def is_odd(e):
    return e%2==1
def odd_list(alist):
    return [e for e in alist if e%2==1]
def sum_square(alist):
    sm = 0
    for i in alist:
        sm+=i**2
    return sm
exec(input().strip())