class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, size):
        self.cache = {}
        self.size = size
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def _insert(self, key, val):

    def _delete(self, key):


    def get(self, key):

        if key not in cache:
            return -1

        node = self.cache[key]

        self._delete(node)
        self._insert(node)


    def put(self, key, val):

        if key in self.cache:
            old = self.cache[key]
            self._delete(old)
            del self.cache[old.key]

        node = Node(key, val)

        self.cache[key] = node
        self._insert(key, node)


        if len(self.cache) == self.size+1:
            removekey = self._delete(self.tail.prev)
            del self.cache[removekey]












cache = LRUCache(3)
print cache.put(1, 10)
print cache.put(2, 20)
print cache.get(1)
print cache.get(3)
print cache.get(2)
print cache.put(2, 40)
print cache.get(2)

