'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-12 11:04:26
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math

free_var_str="x"
dep_var_str="y"

free_var=0
dep_var=0


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
    def trans(self,func_str:str):
        if func_str==free_var_str:
            self.data_stack.append(free_var)
        elif func_str==dep_var_str:
            self.data_stack.append(dep_var)
        else:
            try:
                self.data_stack.append(eval(func_str))
            except:
                self.op_stack.append(func_str)


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

        