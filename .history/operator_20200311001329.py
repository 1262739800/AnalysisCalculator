'''
@Author: your name
@Date: 2020-03-11 00:07:48
@LastEditTime: 2020-03-11 00:13:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /数学分析/function.py
'''
class operator:
    name=None
    def operation(*args):
        pass

class add(operator):
    def __init__(self):
        self.name="+"
    def operation(*args):
        return args[0]+args[1]

class sub(operator):
    def __init__(self):
        self.name="+"
    def operation(*args):
        return args[0]-args[1]

class multi(operator):
    def __init__(self):
        self.name="+"
    def operation(*args):
        return args[0]*args[1]

class dev(operator):
    def __init__(self):
        self.name="+"
    def operation(*args):
        return args[0]/args[1]

