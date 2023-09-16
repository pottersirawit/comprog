def no_lower_case(pw):
    chk = True
    for i in pw:
        if 'a'<=i<='z':
            chk = False
    return chk
def no_upper_case(pw):
    chk = True
    for i in pw:
        if 'A'<=i<='Z':
            chk = False
    return chk 
def no_number_case(pw):
    chk = True
    for i in pw:
        if '0'<=i<='9':
            chk = False
    return chk
def no_symbol_case(pw):
    chk = True
    for i in pw:
        if not ('0'<=i<='9' or 'A'<=i<='Z' or 'a'<=i<='z' ):
            chk = False
    return chk  
def c_repeat(pw):
    chk = False
    for i in range(len(pw)-3):
        if pw[i]==pw[i+1]==pw[i+2]==pw[i+3]:
            chk = True
    return chk
def num_seq(pw):
    chk = False
    for i in range(len(pw)-3):
        if pw[i]+pw[i+1]+pw[i+2]+pw[i+3] in '0123456789' or pw[i]+pw[i+1]+pw[i+2]+pw[i+3] in '0987654321' :
            chk = True
    return chk
def let_seq(pw):
    chk = False
    for i in range(len(pw)-3):
        s = (pw[i]+pw[i+1]+pw[i+2]+pw[i+3]).lower()
        if  s in 'abcdefghijklmnopqrstuvwxyz' or s in 'zyxwvutsrqponmlkjihgfedcba' :
            chk = True
    return chk
def key_pattern(pw):
    chk = False
    for i in range(len(pw)-3):
        s = (pw[i]+pw[i+1]+pw[i+2]+pw[i+3]).lower()
        if  s in '!@#$%^&*()_+' or s in '+_)(*&^%$#@!' or s in 'qwertyuiop' or s in 'poiuytrewq' \
            or s in 'asdfghjkl' or s in 'lkjhgfdsa' or s in 'zxcvbnm' or s in 'mnbvcxz':
            chk = True
    return chk
pw = input().strip() 
error = []
if len(pw) < 8:
    error.append('Less than 8 characters')
if no_lower_case(pw):
    error.append('No lowercase letters')
if no_upper_case(pw):
    error.append('No uppercase letters')
if no_number_case(pw):
    error.append('No numbers')
if no_symbol_case(pw):
    error.append('No symbols')
if c_repeat(pw):
    error.append('Character repetition')
if num_seq(pw):
    error.append('Number sequence')
if let_seq(pw):
    error.append('Letter sequence')
if key_pattern(pw):
    error.append('Keyboard pattern')
if len(error) == 0:
    print('OK')
else:
    for i in error:
        print(i)