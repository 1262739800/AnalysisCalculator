'''
@Author: your name
@Date: 2020-03-08 10:37:21
@LastEditTime: 2020-03-10 23:33:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/recognize.py
'''
import math
import numpy as np

prise = 10e-3


def add(x, y): return x+y


def sub(x, y): return x-y


def multi(x, y): return x * y


def dev(x, y): return x/y


def dif(n, f, x):
    if n == 1:
        return (f(x+prise)-f(x))/prise
    else:
        return (dif(n-1, f, x+prise)-dif(n-1, f, x))/prise


def pow(x, y): return math.pow(x, y)


sign_dict_complex = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": dev,
    "^": math.pow
}

sign_dict_single = {
    "'": dif,
    "cos": math.cos,
    "sin": math.sin,
}
sign_priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "^": 3,
    "'": 4,
    "(": 5,
    ")": 5,
    "sin": 5,
    "cos": 5,

}


def check_priority(data_stack: list, sign_stack: list):
    if sign_priority[sign_stack[-1]] <= sign_priority[sign_stack[-2]]:
        

x=np.array([1:0.1:10])

def recognize_func(func_str: str):
    data_stack = []
    sign_stack = []

    for char in func_str:
        if char == ' ':
            continue
        else:
            if char == 'x' or 'y':
                data_stack.append(char)

            else:
                sign_stack.append(char)
