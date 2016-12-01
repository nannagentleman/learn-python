# -*- coding: utf-8 -*-
class StackUnderflow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elem = [] #_elem中存储栈中元素？
        #为什么用_elem? 不能在初始化stack的时候传入参数？
    
    def is_empty(self):
        return self._elem == []
        #foolish method: use if else...
    
    def top(self):
        if self._elem == []:
            raise StackUnderflow("in SStack.top()")
            #remember to do this step!
        else:
            return self._elem[-1]
            
    def push(self, elem):
        self._elem.append(elem)
        
    def pop(self):
        if self._elem == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elem.pop()