'''
@Author: your name
@Date: 2020-03-08 10:30:14
@LastEditTime: 2020-03-08 10:58:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/de.py
'''
import sys
import recognize as re
import calculate as cal


def main():
    while True:
        func_str=input("please enter your equition with free variable x and depend variable y:")
        re.recognize_func(func_str)
        ans_str=input("please enter your answer with free variable x and depend variable y:")
        re.recognize_func(ans_str)

if __name__=="__main__":
    main()

