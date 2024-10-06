#鸡兔同笼

a=int(input())
if a%2==0:
    if a%4==0:
        b=int(a//4)
        c=int(a//2)
        print(b,c)
    else:
        b=int(a//4+1)
        c=int(a//2)
        print(b,c)
else:
    print(0,0)