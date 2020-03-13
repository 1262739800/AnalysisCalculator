'''
@Author: your name
@Date: 2020-03-10 23:46:38
@LastEditTime: 2020-03-12 11:15:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/recog.py
'''
import operator as op
from operator import operator_dict as op_dict
from operator import calculator

def is_one_word(l1:str,l2:str):
    if l1.isdigit()and l2.isdigit():
        return True
    elif l1.isalpha() and l2.isalpha():
        return True
    elif  (not l1.isalnum()) & (not l2.isalnum()):
        return True
    else:
        return False

def split(func_str:str):
    temp=""
    split_func=[]
    for x in func_str:
        if x == " ":
            continue
        elif len(temp)==0 or is_one_word(temp[-1],x):
            temp+=x
        else:
            split_func.append(temp)
            temp=x
    if len(temp) != 0:
        split_func.append(temp)
    return split_func

    
def calculate(split_func:list):
    for x in split_func:
        x=trans(x)
        if type(x)==int or float:
            data_stack.append(x)
        elif type(x)==str:
            if x =='('or')':
                op_stack.append(x)                
            else:
                op_stack.append(op_dict[x])
            
def check_priority():

            

print(split("x*y+523*6+7"))
cal=op.calculator
