from collections import OrderedDict


class LRUCache:

    # initialising default constructor
    # initializing max capacity of cache
    def __init__(self, maximum_capacity: int):
        self.cache = OrderedDict()
        self.size = maximum_capacity

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value  # mapping key with value
        self.cache.move_to_end(key)  # putting them in last
        if len(self.cache) > self.size:  # checking if the cache maximum size limit exceeding or not.
            self.cache.popitem(last=False)  # if exceed the maximum size then pop "Least Recent Used Item"

    # implementation of get function from cache using key
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # return -1 if no key found
        else:
            self.cache.move_to_end(key)  # pushing value to the end of cache
            return self.cache[key]  # return value of the key

    # implementation of delete function from cache using key
    def delete(self, key: int) -> bool:
        if key not in self.cache:
            return False  # return false if no key found
        else:
            self.cache.pop(key)
            return True  # return true if deleted

    def reset(self) -> bool:
        self.cache = ""  # resetting all value
