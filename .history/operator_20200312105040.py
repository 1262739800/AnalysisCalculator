'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-12 10:50:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math


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
}

class calculator:
    data_stack=[]
    op_stack=[]


class operator:
    name=None
    def operation(*args):
        pass

class add:
    def __init__(self):
        super().__init__()
        super.name="+"
    def operation(*args):
        return args[0]+args[1]

        