'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions: Follow up: How would you handle collisions in HashMap?

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
'''

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
        self.size = 100
        self.hash_map = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        slot = key % self.size              
        curr = self.hash_map[slot]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
            
        node = Node(key,value)
        node.next = self.hash_map[slot]
        self.hash_map[slot] = node

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        slot = key % self.size
        curr = self.hash_map[slot]
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
        curr = self.hash_map[slot]
        while curr:
            if curr.key == key:
                curr.key = -1
                return
            curr = curr.next
        
        return

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,0)
obj.put(1,10)
obj.put(2,2)
obj.put(2,12)
param_2 = obj.get(1)
obj.remove(1)

