'''
@Author: your name
@Date: 2020-03-07 15:51:02
@LastEditTime: 2020-03-07 21:26:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/compute.py
'''
import math as m
y1=lambda x:(-2*x*x-5*x-3)*m.exp(2*x)
dif=lambda n,f,x:1000*f(x+0.001)-1000*f(x) if n==1 else 1000*dif(n-1,f,x+0.001)-1000*dif(n-1,f,x)

F=lambda y,x:dif(2,y,x)-6*dif(1,y,x)+9*y(x)-(x+1)*m.exp(2*x)
y2=lambda x:(x+1)

w=lambda x:x*m.exp(x)

x=10

print(F(y1,x))