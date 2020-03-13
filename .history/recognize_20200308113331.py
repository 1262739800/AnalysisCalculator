'''
@Author: your name
@Date: 2020-03-08 10:37:21
@LastEditTime: 2020-03-08 11:33:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/recognize.py
'''
import math

sign_dict = {
    "+": add,
    "-": sub}

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


def recognize_func(func_str: str):
    data_stack = []
    sign_stack = []
    for char in func_str:
        print(char, end="")
