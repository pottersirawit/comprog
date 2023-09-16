filename = input()
cmd = input()
if cmd != 'LSTRIP' and cmd != 'RSTRIP' and cmd != 'STRIP' and cmd != 'STRIP_ALL':
    print('Invalid command')
    exit(0)
fn = open(filename,'r')
lm = 9999
rm = -9999
for line in fn:
    line = line.strip()
    for i in range (len(line)):
        if line[i] !='.':
            lm = min(lm,i)
            rm = max(rm,i)
fn.close()
if cmd == 'LSTRIP':
    fn = open(filename,'r')
    for line in fn:
        line = line.strip()
        print(line[lm:])
    fn.close()
if cmd == 'RSTRIP':
    fn = open(filename,'r')
    for line in fn:
        line = line.strip()
        print(line[:rm+1])
    fn.close()
if cmd == 'STRIP':
    fn = open(filename,'r')
    for line in fn:
        line = line.strip()
        print(line[lm:rm+1])
    fn.close()
if cmd == 'STRIP_ALL':
    s = []
    fn = open(filename,'r')
    for line in fn:
        s.append(line[lm:rm+1])
    fn.close()
    chk = [False for i in range(len(s[0]))]
    for e in s:
        for i in range(len(e)):
            if e[i] != '.':
                chk[i] |= True
    for e in s:
        for i in range(len(e)):
            if chk[i]:
                print(e[i],end='')
        print()