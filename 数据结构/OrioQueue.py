class PrioQueueError(ValueError):
    pass

class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap() #what?
            
    def is_empty(self):
        return not self._elems
        
    def peek(self):
        if self.isempty():
            raise PrioQueueError("in peek")
        return self._elems[0]
        
    def enqueue(self, e):
        self._elems.append(None) 
        self.siftup(e, len(self.elems)-1)
    
    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)//2
        
        
    