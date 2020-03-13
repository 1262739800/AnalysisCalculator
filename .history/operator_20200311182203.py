'''
@Author: your name
@Date: 2020-03-11 00:07:48
@LastEditTime: 2020-03-11 18:22:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math

data_stack=[]
sign_stack=[]

class operator:
    name=None

class add(operator):
    def __init__(self):
        return args[0]+args[1]

class sub(operator):
    def __init__(self):
        return args[0]-args[1]

class multi(operator):
    def __init__(self):
        return args[0]*args[1]

class dev(operator):
    def __init__(self):
        return args[0]/args[1]

operator_dict = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": dev,
    "^": math.pow,}
'''   "'": dif,
    "cos": math.cos,
    "sin": math.sin,'''

