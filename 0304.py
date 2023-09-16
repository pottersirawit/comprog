mb = input()
if len(mb) != 10:
    print("Not a mobile number")
else :
    if mb[0:2] == '06' or mb[0:2] == '08' or mb[0:2] == '09':
        print("Mobile number")
    else :
        print("Not a mobile number")