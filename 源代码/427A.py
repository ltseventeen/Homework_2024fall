n=int(input())
events=list(map(int,input().split()))

#初始化计数器
police=0
untreated_crime=0

#读取每一个事件，不是招人就是犯罪
for x in range(n):
    if 0<events[x]<=10:#招人
        police+=events[x]
    elif events[x]==-1:
        if police>0:#有人就治理犯罪
            police-=1
        elif police==0:#没有人就继续犯罪
            untreated_crime+=1

#输出结果
print(untreated_crime)