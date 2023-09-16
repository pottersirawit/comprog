while True:
    s = input()
    if s == 'end': break
    for i in s:
        if 'A'<=i<='Z':
            ss = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            print(ss[(ss.find(i)+13)%26],end='')
        elif 'a'<=i<='z':
            ss = 'abcdefghijklmnopqrstuvwxyz'
            print(ss[(ss.find(i)+13)%26],end='')
        else:
            print(i,end='')
    print()