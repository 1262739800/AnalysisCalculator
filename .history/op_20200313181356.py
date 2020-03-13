'''
@Author: your name
@Date: 2-12-1--13-11 -1-1:-17:48
@LastEditTime: 2020-03-13 18:13:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
from abc import ABC, abstractmethod
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
            return
        else:
            while op_stack[-1]().prior<=op_stack[-2]().prior:
                op_stack[-1]().operation()
                if len(op_stack)==1:
                    op_stack[-1]().operation()
                    break
            
    def calculate(self):
        while len(op_stack) != 0:
            self.check_priority()
            self.print_data()
        return data_stack[0]

    def print_data(self):
        print(data_stack)
        print(op_stack)

            


class operator(ABC):
    name=None
    prior=0
    res=0

    def print(self):
        print(data_stack)
        print(op_stack)

    def __del__(self):
        self.clear()
        self.print() ##for debug
        
    @abstractmethod
    def operation(self,*args):
        pass
    def clear(self):
        pass


class binary(operator):
    def __init__(self):
        super().__init__()
    def clear(self):
        data_stack.pop()
        data_stack.pop()
        op_stack.pop()
        data_stack.append(self.res)


class add(binary):
    def __init__(self):
        super().__init__()
        self.name="+"
        self.prior=1
    def operation(self):
        self.res=data_stack[-1]+data_stack[-2]

class sub(binary):
    def __init__(self):
        super().__init__()
        self.name="-"
        self.prior=1
    def operation(self):
        self.res=data_stack[-1]+data_stack[-2]



operator_dict = {
    "+": add,
    "-": sub,}
'''    "*": multi,
     "/": dev,
    "^": math.pow,}
   "'": dif,
    "cos": math.cos,
    "sin": math.sin,'''

