n,m,a=map(int,input().split())
if n%a!=0 and m%a!=0:
 x=n//a+1
 y=m//a+1
 print(x*y)
elif n%a!=0 and m%a==0:
    x=n//a+1
    y=m//a
    print(x*y)
elif n%a==0 and m%a!=0:
    x=n//a
    y=m//a+1
    print(x*y)
else:
    x=n//a
    y=m//a
    print(x*y)