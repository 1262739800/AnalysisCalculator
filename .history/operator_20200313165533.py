'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-13 16:55:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
import math

free_var_str="x"
dep_var_str="y"

free_var=0
dep_var=0

data_stack=[]
op_stack=[]


class calculator:
    def trans(self,func_str:str):
        if func_str==free_var_str:
            data_stack.append(free_var)
        elif func_str==dep_var_str:
            data_stack.append(dep_var)
        else:
            try:
                data_stack.append(eval(func_str))
            except:
                op_stack.append(operator_dict[func_str])

    def check_priority(self):
        if op_stack[-1]().name=='(':
            pass
        elif op_stack[-1]().prior<op_stack[-1]().prior:
            op_stack[-1]().operation()
            self.check_priority(self)
            
    def calculate(self):
        while len(op_stack) is not 0:
            check_priority(self)
            self.print_data(self)
        return data_stack[0]

    def print_data(self):
        print(data_stack)
        print(op_stack)

            


class operator:
    name=None
    prior=0
    def operation(*args):
        pass

class add:
    def __init__(self):
        super().__init__()
        super.name="+"
        super.prior=1
    def operation():
        res=data_stack[-1]+data_stack[-2]
        data_stack.pop()
        data_stack.pop()
        op_stack.pop()
        data_stack.append(res)



operator_dict = {
    "+": add,}
'''    "-": sub,
    "*": multi,
    "/": dev,
    "^": math.pow,}
   "'": dif,
    "cos": math.cos,
    "sin": math.sin,'''

