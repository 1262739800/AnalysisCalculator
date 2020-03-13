'''
@Author: your name
@Date: 2020-03-08 10:30:14
@LastEditTime: 2020-03-08 10:49:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/de.py
'''
import sys
import recognize.py


def main():
    while True:
        func_string=input("please enter your equition with free variable x and depend variable y:")
        recognize_func(func_string)
        print(func_string)


if __name__=="__main__":
    main()

