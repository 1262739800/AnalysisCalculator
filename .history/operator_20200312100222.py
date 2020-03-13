'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-12 10:02:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math

data_stack=[]
op_stack=[]


def add():
    res=data_stack[-1]+data_stack[-2]
    del data_stack[-1] 
    del data_stack[-2]
    return res

def sub( ): 
    res=data_stack[-1]-data_stack[-2]
    del data_stack[-1] 
    del data_stack[-2]
    return res

def multi( ):
    res=data_stack[-1]*data_stack[-2]
    del data_stack[-1] 
    del data_stack[-2]
    return res

def dev( ):
    res=data_stack[-1]/data_stack[-2]
    del data_stack[-1] 
    del data_stack[-2]
    return res

 operator_dict = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": dev,
    "^": math.pow,}
'''   "'": dif,
    "cos": math.cos,
    "sin": math.sin,'''

data_stack.extend([0,1,2,3])
print( _dict["+"]())