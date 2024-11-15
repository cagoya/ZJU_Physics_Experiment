# 计算平均值和A类不确定度，直接输入数据即可
import math

l=list(float,input().split())
n=len(l)
sum=0
for i in l:
    sum+=i
avg=sum/n
print("average = {}".format(avg))
u_a=0
for i in l:
    u_a+=(i-avg)**2
u_a=u_a/(n*(n-1))
u_a=u_a**0.5
print("u_a = {}".format(u_a))