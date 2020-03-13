'''
@Author: your name
@Date: 2020-03-08 10:30:14
@LastEditTime: 2020-03-08 10:38:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/de.py
'''
import sys
import recognize

if __name__=="__main__":
    main()

def main():
    if len(sys.argv) == 1:
        print ("please enter your equition with free variable x and depend variable y:")
    else :
        recognize_func(sys.argv[1])