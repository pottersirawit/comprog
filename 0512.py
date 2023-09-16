a = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
b = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']
N = int(input())
for i in range(N):
    s = input().strip()
    if s not in a and s not in b:
        print('Not found')
    elif s in a:
        print(b[a.index(s)])
    else :
        print(a[b.index(s)])