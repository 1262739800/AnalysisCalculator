'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-11 18:48:16
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
        return data_stack[-1]+data_stack[-2]

class sub(operator):
    def __init__(self):
        return data_stack[-1]-data_stack[-2]

class multi(operator):
    def __init__(self):
        return data_stack[-1]*data_stack[-2]

class dev(operator):
    def __init__(self):
        return data_stack[-1]/data_stack[-2]

operator_dict = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": dev,
    "^": math.pow,}
'''   "'": dif,
    "cos": math.cos,
    "sin": math.sin,'''

