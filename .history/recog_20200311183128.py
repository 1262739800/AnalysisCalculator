'''
@Author: your name
@Date: 2020-03-10 23:46:38
@LastEditTime: 2020-03-11 18:31:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/recog.py
'''
import operator as op
from operator import operator_dict as op_dict
from operator import data_stack
from operator import sign_stack

free_var="x"
dep_var="y"

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

def trans(func_str:str):
    try:
        return op_dict[func_str]
    except:
        if func_str == '(' or ')':
            return func_str
        else:
            return eval(func_str)
    
def calculate(split_func:list):
    for x in split_func:
        x=trans(x)
        if x

print(split("x*y+523*6+7"))
