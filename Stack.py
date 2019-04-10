class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_stack = []
        

    def push(self, x):
        """
        Push element x to the back of stack.
        :type x: int
        :rtype: void
        """
        if self.min_stack:
            self.min_stack.append((x,min(self.min_stack[-1][1],x)))
        else:
            self.min_stack.append((x,x))
        
        

    def pop(self):
        """
        Removes the element from the top of stack and returns that element.
        :rtype: void
        """
        if self.min_stack:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][1]
    
    def print_stack(self):
        print(self.min_stack)

s = MyStack()
s.push(2)
s.print_stack()
s.push(3)
s.print_stack()
s.pop()
s.print_stack()
print(s.getMin())