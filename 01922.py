import math

#定义到达时间函数
def charley_arrival_time(riders):
    distance = 4.5 #公里数
    charley_time=float('inf')#Charley的到达时间初始化为无穷大

    for speed,start_time in riders:
        if start_time>=0:#如果出发时间大于等于0，则Charley有可能跟随
            riders_time=distance/speed*3600+start_time#计算每个骑手的到达时间
            charley_time=min(charley_time,riders_time)#更新Charley的到达时间

    return math.ceil(charley_time)#返回Charley的到达时间，向上取整


#读取输入，人数以及每个人的速度和出发时间
while True:#死循环，目的是读取输入的每个N后根据N是否为零判断是否退出循环
    N=int(input())
    if N==0:
        break

    riders=[]#初始化每个人速度和出发时间列表
    for _ in range(N):
        speed,start_time=map(int,input().split())
        riders.append((speed,start_time))
    print(charley_arrival_time(riders))#调用到达时间函数并打印结果

