class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue)==0
    
    def print_queue(self):
        print(self.queue)

q = MyQueue()
q.push(2)
q.print_queue()
q.push(3)
q.print_queue()
q.pop()
q.print_queue()
print(q.empty())