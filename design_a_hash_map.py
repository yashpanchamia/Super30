class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hash = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        slot = key % self.size              
        curr = self.hash[slot]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
            
        node = Node(key,value)
        node.next = self.hash[slot]
        self.hash[slot] = node

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        slot = key % self.size
        curr = self.hash[slot]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        slot = key % self.size
        curr = self.hash[slot]
        while curr:
            if curr.key == key:
                curr.key = -1
                return
            curr = curr.next
        
        return