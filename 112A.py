#读取输入的两个字符串并转化为小写
str1=input().lower()
str2=input().lower()

#判断两个字符串的大小关系，字典顺序在python里是内置自带的，根据ASCII码进行比较
if str1<str2:
    print(-1)
elif str1>str2:
    print(1)
else:
    print(0)