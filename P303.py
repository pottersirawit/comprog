fname = input()
k = int(input())
ruler = ''
for i in range(k//10) :
    ruler += '-'*9 + str(i+1) # เพิ่มรอบละ 9 ขีด ตามด้วยตัวเลข
ruler += '-'*(k-(k//10)*10) # เพิ่มที่เหลือ (ถ้ามี)
print(ruler)
s = ''
fn = open(fname,'r')
for line in fn:
    s+=line.strip()+'.'
fn.close()
s+='.'
ans = ''
word = ''
for i in range (len(s)):
    if s[i] == '.':
        if s[i-1]!='.': #before . is word
            if len(ans+word) > k:
                print(ans.strip('.'))
                ans=word+'.'
                word = ''
            else :
                ans+=word+'.'
                word = ''
        else :
            ans+='.'
    else:
        word+=s[i]
print(ans.strip('.'),end='')