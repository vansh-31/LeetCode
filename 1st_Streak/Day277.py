# Problem : Design HashMap
# Problem Statement : Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
class MyHashMap:

    def __init__(self):
        self.hsh = [-1] * (50 + 10**6)
        
    def put(self, key: int, value: int) -> None:
        self.hsh[key] = value

    def get(self, key: int) -> int:
        return self.hsh[key]

    def remove(self, key: int) -> None:
        self.hsh[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)