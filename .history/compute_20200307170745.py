'''
@Author: your name
@Date: 2020-03-07 15:51:02
@LastEditTime: 2020-03-07 17:07:45
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/compute.py
'''
import math as m
answer=lambda x:(x+1)/m.exp(1)*m.log(x/x+1)+1/m.exp(1)
dif=lambda n,f,x:1000*f(x+0.001)-1000*f(x) if n==1 else 1000*dif(n-1,f,x+0.001)-1000*dif(n-1,f,x)

F=lambda y,x:x*dif(2,y,x)-(1+x)*dif(1,y,x)+y(x)
answer1=lambda x:(x+1)
print(F(answer,5))

print(F(answer1,1)