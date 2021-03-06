'''
@Author: your name
@Date: 2020-03-10 23:46:38
@LastEditTime: 2020-03-11 00:47:12
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/recog.py
'''
import operator as op


data_stack=[]
sign_stack=[]

def is_one_word(l1:str,l2:str):
    if l1.isdigit()and l2.isdigit():
        return 1
    elif l1.isalpha() and l2.isalpha():
        return 2
    elif  not (l1.isalnum() and l1.isalnum()):
        return 3
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
        
print(split("x*y+523*6+7"))
print(is_one_word("*","y"))