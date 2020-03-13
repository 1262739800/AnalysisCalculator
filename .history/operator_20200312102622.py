'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-12 10:26:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math



def add():
    res=data_stack[-1]+data_stack[-2]
    del data_stack[-1] 
    del data_stack[-1]
    return res

def sub( ): 
    res=data_stack[-1]-data_stack[-2]
    del data_stack[-1] 
    del data_stack[-1]
    return res

def multi( ):
    res=data_stack[-1]*data_stack[-2]
    del data_stack[-1] 
    del data_stack[-1]
    return res

def dev( ):
    res=data_stack[-1]/data_stack[-2]
    del data_stack[-1] 
    del data_stack[-1]
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

op_priority={
    "+":1,
    "-":1,
    "*"=2,
    "/"=2,
    "("=100,
}

class calculator:
    data_stack=[]
    op_stack=[]


class operator:
    
    def operation(*args):
        pass