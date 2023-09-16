dna = input().strip().upper()
order = input().strip()
if order =='D': pp =input().strip()
chk = True
for i in dna:
    if i not in 'ATCG':
        chk=False
if not chk:
    print('Invalid DNA')
else :
    if order == 'R':
        ans=''
        for i in dna:
            if i == 'A' : ans+='T'
            if i == 'T' : ans+='A'
            if i == 'G' : ans+='C'
            if i == 'C' : ans+='G'
        print(ans[::-1])
    elif order == 'F':
        a,t,c,g =0,0,0,0
        for i in dna:
            if i == 'A' : a+=1
            if i == 'T' : t+=1
            if i == 'G' : g+=1
            if i == 'C' : c+=1
        print('A='+str(a)+', T='+str(t)+', G='+str(g)+', C='+str(c))
    elif order == 'D':
        ans=0
        for i in range (len(dna)-1):
            if dna[i]+dna[i+1] == pp:
                ans+=1
        print(ans)