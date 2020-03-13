'''
@Author: your name
@Date: 2020-03-11 00:07:48
@LastEditTime: 2020-03-11 00:12:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
class operator:
    def __init__(self):
        super().__init__()
    name=None
    def operation(*args):
        pass

class add(operator):
    def __init__(self):
        self.name="+"
    
    def operation(*args):
        return args[0]+args[1]