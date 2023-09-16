d1 = {}
d2 = {}
d3 = {}
n = int(input())
for i in range(n):
    s1,s2 = input().split(':')
    s2 = s2.strip()
    s3 = s2.split(', ')
    d3[s1] = i
    d1[s1] = s3
    for i in s3:
        if i not in d2:
            d2[i] = [s1]
        else:
            d2[i].append(s1)
q = input()
print_pi_laew = [q]
ans = []
for i in d1[q]:
    for j in d2[i]:
        if j not in print_pi_laew:
            chk = 0
            ans.append([d3[j],j])
            print_pi_laew.append(j)
ans.sort()
if len(ans)==0:print('Not Found')
else:
    for i in ans:
        print(i[1])