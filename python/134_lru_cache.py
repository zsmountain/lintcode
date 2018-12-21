'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.cache = {}
        self.capacity = capacity
        self.dummy_tail = self.dummy_head = DoubleLinkedListNode(-1, -1)
        self.dummy_tail.pre = self.dummy_head
        self.dummy_head.next = self.dummy_tail

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.append_node(node)
        return self.cache[key].value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                head = self.dummy_head.next
                self.remove_node(head)
                del self.cache[head.key]
            node = DoubleLinkedListNode(key, value)
            self.append_node(node)
            self.cache[key] = node
        else:
            self.cache[key].value = value
            self.remove_node(self.cache[key])
            self.append_node(self.cache[key])
    
    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def append_node(self, node):
        tail = self.dummy_tail.pre
        node.pre = tail
        self.dummy_tail.pre = node
        tail.next = node
        node.next = self.dummy_tail


cache = LRUCache(2)
cache.set(2, 1)
cache.set(1, 1)
print(cache.get(2))
cache.set(4, 1)
print(cache.get(1))
print(cache.get(2))

cache = LRUCache(1)
cache.set(2, 1)
print(cache.get(2))
cache.set(3, 2)
print(cache.get(2))
print(cache.get(3))
        
