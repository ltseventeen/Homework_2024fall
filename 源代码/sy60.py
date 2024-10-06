#读取[a,b]
a,b=map(int,input().split())
flower_number=[]#初始化列表

#遍历[a,b]中的所有整数,从小到大读取，判断是不是水仙花数
for i in range(a,b+1):
    x,y,z=i//100,i%100//10,i%100%10//1
    if i==x**3+y**3+z**3:
        flower_number.append(str(i))

#输出结果
if len(flower_number)==0:
    print('NO')
else:
    result=' '.join(flower_number)#用空格分隔输出结果,注意join后面的可迭代对象的每一个元素必须是字符串
    print(result)