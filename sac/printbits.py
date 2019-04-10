from bit4 import bitmode_4
from bit5 import bitmode_5

def bit4print(x):
    print(x, end='  ')
    print(bitmode_4().twoscomp4(x) , end='  ')
    print(bitmode_4().onescomp4(x) , end='  ')
    print(bitmode_4().unsigned4(x) , end='  ')
    print(bitmode_4().signed4(x))

def bit5print(x):
    print(x, end='  ')
    print(bitmode_5().twoscomp5(x) , end='  ')
    print(bitmode_5().onescomp5(x) , end='  ')
    print(bitmode_5().unsigned5(x) , end='  ')
    print(bitmode_5().signed5(x))

def bitprint(x,n):
    if n == '4':
        bit4print(x)
    else:
        bit5print(x)

def addprint(a,b,n):
    if n == '4':
        a1 = bitmode_4().binary4(a,b)
        a2 = bitmode_4().twoscomp4(a) + bitmode_4().twoscomp4(b)
        a3 = bitmode_4().onescomp4(a) + bitmode_4().onescomp4(b)
        a4 = bitmode_4().unsigned4(a) + bitmode_4().unsigned4(b)
        a5 = bitmode_4().signed4(a) + bitmode_4().signed4(b)
    elif n == '5':
        a1 = bitmode_5().binary5(a,b)
        a2 = bitmode_5().twoscomp5(a) + bitmode_5().twoscomp5(b)
        a3 = bitmode_5().onescomp5(a) + bitmode_5().onescomp5(b)
        a4 = bitmode_5().unsigned5(a) + bitmode_5().unsigned5(b)
        a5 = bitmode_5().signed5(a) + bitmode_5().signed5(b)
    print("Binary Rep : " , end='')
    print(a1 , end='')
    if n=='4' and int(int(a1)/10000) == 1:
        print(" (Overflow)")
    elif n=='5' and int(int(a1)/100000) ==1:
        print(" (Overflow)")
    else:
        print("")
    print("2's comp   : " , end='')
    print(a2 , end='')
    if a2<-pow(2, int(n)-1) or a2>pow(2, int(n)-1)-1:
        print(" (Overflow)")
    else:
        print("")
    print("1's comp   : " , end='')
    print(a3 , end='')
    if a3<-(pow(2, int(n)-1)-1) or a3>pow(2, int(n)-1)-1:
        print(" (Overflow)")
    else:
        print("")
    print("Unsigned   : " , end='')
    print(a4 , end='')
    if a4>pow(2, int(n))-1:
        print(" (Overflow)")
    else:
        print("")
    print("Signed     : " , end='')
    print(a5 , end='')
    if a5<-(pow(2, int(n)-1)-1) or a5>pow(2, int(n)-1)-1:
        print(" (Overflow)")
    else:
        print("")
