#读取输入
t=int(input())
for _ in range(t):#每次读取一组a,ba
    a,b=map(int,input().split())
    if a%b!=0:#看a是否能被b整除
        move=b-(a%b)
    else:
        move=0
    print(move)