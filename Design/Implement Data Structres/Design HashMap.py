'''
Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:
MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
'''
class MyHashMap:
    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
    
    def __init__(self):
        self.nodes = [None] * 10000
        
    def hashCode(self, index):
        return index % len(self.nodes)
    
    def put(self, key, value):
        bucket = self.hashCode(key)
        if not self.nodes[bucket]:
            self.nodes[bucket] = self.ListNode(-1, -1)
        
        prev = self.find(self.nodes[bucket], key)
        
        if not prev.next:
            prev.next = self.ListNode(key, value)
        else:
            prev.next.value = value
    
    def find(self, node, key):
        prev = None
        while node and node.key != key:
            prev = node
            node = node.next
        return prev
    
    def get(self, key):
        bucket = self.hashCode(key)
        
        if not self.nodes[bucket]:
            return -1
        
        search = self.find(self.nodes[bucket], key)
        
        return -1 if not search.next else search.next.value
    
    def remove(self, key):
        bucket = self.hashCode(key)
        if not self.nodes[bucket]:
            return
        
        prev = self.find(self.nodes[bucket], key)
        if prev.next:
            prev.next = prev.next.next

