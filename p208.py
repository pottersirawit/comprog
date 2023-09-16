def to_Thai( N ):
    list = ['','neung','song','sam','si','ha','hok','chet','paet','kao']
    ans = ''
    if N >= 1000:
        ans += list[N//1000]
        ans += ' pun '
        N%=1000
    if N >= 100:
        ans += list[N//100]
        ans += ' roi '
        N%=100
    if N >= 10:
        list = ['','','yi','sam','si','ha','hok','chet','paet','kao']
        ans += list[N//10]
        ans += ' sip '
        N%=10
    if N==1:
        if len(ans)==0:ans+='neung'
        else:ans+='et'
    elif N==0:
        if len(ans)==0:ans+='soon'
    else :
        list = ['','neung','song','sam','si','ha','hok','chet','paet','kao']
        ans+=list[N]
    return ans.strip()
exec(input().strip()) 