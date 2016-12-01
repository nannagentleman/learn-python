class StackUnderflow(ValueError):
    pass

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
        
class LStack:
    def __init__(self):
        self._top = None
        
    def is_empty(self):
        return self._top is None
        
    def top(self):
        if self._top is None:
            raise StackUnderflow("in Lstack.top()")
        return self._top.elem #why? .elem?
    
    def push(self, elem):
        self._top = LNode(elem, self._top)
        
    def pop(self):
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem
        
st1 = LStack()
st1.push(3)
st1.push('e')
while not st1.is_empty():
    print st1.pop()
        
        