'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-11 23:47:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math

data_stack=[]
op_stack=[]

class operator:
    name=None

class add(operator):
    def __init__(self):
        res=data_stack[-1]+data_stack[-2]
        del data_stack[-1] 
        del data_stack[-2]
        return res

class sub(operator):
    def __init__(self):
        res=data_stack[-1]-data_stack[-2]
        del data_stack[-1] 
        del data_stack[-2]
        return res

class multi(operator):
    def __init__(self):
        res=data_stack[-1]*data_stack[-2]
        del data_stack[-1] 
        del data_stack[-2]
        return res

class dev(operator):
    def __init__(self):
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

