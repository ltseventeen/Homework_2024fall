#输入5*5的矩阵
matrix=[[int(x) for x in input().split()]for _ in range(5)]

#确定1的为位置
for i in range(5):
    for j in range(5):
        if matrix[i][j]==1:
            move=abs(i-2)+abs(j-2)#计算移动的步数

print(move)