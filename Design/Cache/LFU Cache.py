'''
Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the LFUCache class:
LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''
from collections import defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.key_count = {}
        self.key_lru = defaultdict(list)
        self.min = -1
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        count = self.key_count[key]
        # Remove from the key_lru since the count of kye is increased
        self.key_lru[count].remove(key)

        # If the count of key accessed was min and if there are no more min keys in the set, then we increase the min
        if count == self.min and not self.key_lru[count]:
            self.min += 1
            del self.key_lru[count]
        
        # Update the key count and set
        self.put_count(key, count + 1)
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return
        else:
            if len(self.cache) >= self.capacity:
                #  we used FIFO for list. i.e. element at 0th position will be least recently used
                evict_key = self.key_lru[self.min].pop(0)
                del self.cache[evict_key]
                del self.key_count[evict_key]
            
            # Since we are adding a new element, we update min to 1
            self.min = 1
            self.put_count(key, self.min)
            self.cache[key] = value

    def put_count(self, key, count):
        self.key_count[key] = count
        self.key_lru[count].append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
