d = { 'a' : '2' , 'b' : '22' , 'c' : '222' , \
'd' : '3' , 'e' : '33' , 'f' : '333' ,\
'g' : '4' , 'h' : '44' , 'i' : '444' ,\
'j' : '5' , 'k' : '55' , 'l' : '555' ,\
'm' : '6' , 'n' : '66' , 'o' : '666' ,\
'p' : '7' , 'q' : '77' , 'r' : '777' , 's' : '7777' ,\
't' : '8' , 'u' : '88' , 'v' : '888' ,\
'w' : '9' , 'x' : '99' , 'y' : '999' , 'z' : '9999' , ' ' : '0'
}
def text2keys(text):
    ans = []
    text = text.lower()
    for i in text:
        if i in d:
            ans.append(d[i])
    return ' '.join(ans)
def keys2text( keys ):
    ans = []
    d2 = {}
    for i in d:d2[d[i]] = i
    keys = keys.strip().split()
    #print(keys)
    for i in keys:
        ans.append(d2[i])
    return ''.join(ans)
exec(input().strip())