n=int(input())#输入题目数量

solved_problems=0#记录已解决题目的数量

for i in range(n):#遍历题目（0-（n-1））
    a,b,c=map(int,input().strip().split())#每排的0或1,map的作用是将输入的字符串转化为int类型，语法为map（函数，序列）
    if a+b+c>=2:
        solved_problems+=1#如果题目有两个以上1，则加1
    else:
        solved_problems+=0#否则不加,也可以用continue！！3

print(solved_problems)#输出已解决题目的数量