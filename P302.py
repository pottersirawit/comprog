s = input().strip()
if len(s) <=3:
    check_col = True
    check_row = True
    check_col &= ('a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z')
    if len(s) == 1 : check_row = not True
    if len(s) == 2:check_row &= s[1] in '123456789'
    if len(s) == 3:
        check_row &= (s[1] in '0123456789' or s[1] ==' ')
        check_row &= s[2] in '0123456789'
        if check_row:
            check_row &=  0 < int(s[1:]) < 53
    if check_col and check_row:
        if (ord(s[0]) + int(s[1:])) % 2 == 0:print('White')
        else:print('Black')
    else:
        if not check_col and not check_row : print('Invalid row and column')
        elif not check_col:print('Invalid row')
        else :print('Invalid column')
else:
    d = {}
    A,B = s.split(',')
    A = A.strip();B = B.strip()
    A0,A1 = A.split('=')
    A0 = A0.strip();A1 = A1.strip()
    d[A0] = A1
    B0,B1 = B.split('=')
    B0 = B0.strip();B1 = B1.strip()
    d[B0] = B1
    check_col = True
    check_row = True
    #print(d['row'],d['col'])
    if len(d['row']) == 0 and len(d['col']) == 0:
        check_col = not True
        check_row = not True
    if len(d['row']) == 0:
        check_row = not True
    if len(d['col']) == 0:
        check_col = not True
    if check_row:
        check_row &= len(d['row']) == 1
        check_row &= ('a' <= d['row'][0] <= 'z' or 'A' <= d['row'][0] <= 'Z')
    if check_col:
        try :check_col &=  0 < int(d['col']) < 53
        except :check_col = False
    if check_col and check_row:
        if (ord(d['row'][0]) + int(d['col'])) % 2 == 0:print('White')
        else:print('Black')
    else:
        if not check_col and not check_row : print('Invalid row and column')
        elif not check_col:print('Invalid column')
        else :print('Invalid row')