filename = input().strip()
fn = open(filename,'r')
code = fn.readline().strip()
pattern = fn.readline().strip()
while True:
    text = fn.readline().strip()
    if len(text)==0:break
    if code == 'T2M':
        morse = ''
        for e in text :
            j = pattern.find('[' + e + ']')
            if j==-1:
                morse = 'Invalid : '+text
                break
            j += 3
            k = pattern.find('[',j)
            morse += pattern[j:k] + ' '
        print(morse.strip())
    elif code == 'M2T':
        text2 = text.split()
        ans = ''
        for e in text2 :
            j = pattern.find(']' + e + '[')
            if j==-1:
                ans = 'Invalid : '+text
                break
            ans += pattern[j-1]
        print(ans)
    else :
        print('Invalid code')
fn.close()