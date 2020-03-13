'''
@Author: your name
@Date: 2020-03-08 10:30:14
@LastEditTime: 2020-03-13 23:23:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/de.py
'''
import sys
import recog 


def main():
    while True:
        func_str=input("please enter formula\n")
        cal=calculator()
        cal.calculate(func_str)

if __name__=="__main__":
    main()

