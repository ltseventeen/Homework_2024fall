#先读取路的长度和建路的段数
L,M=map(int,input().split())
#建立种树列表
trees=[1]*(L+1)

#每一段铁路砍树
for _ in range(M):
    a,b=map(int,input().split())#读取起止点
    for i in range(a,b+1):#遍历（a,b)段里的所有树，注意不含结束点，所以要是b+1
        trees[i]=0#砍掉树

#统计剩余的树的数量
print(trees.count(1))