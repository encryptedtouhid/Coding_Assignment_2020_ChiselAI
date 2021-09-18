# Coding Assignment 2020 ( ChiselAI )

## Files

#### `LRUCache.py`
File containing `LRUCache` class and "put" , "get", "delete" , "reset" function for LRUCache.

#### `main.py`
File containing how to use `LRUCache` functions.

## LRUCache Syntax
` cache = LRUCache(`maximum_capacity`)`

**Parameters**

`maximum_capacity`: this number indicates the maximum size of the cache can store

## LRUCache Functions

- `put(key, value)`

   Add a key-value pair with key: `key` and value: `value` to the cache.
   If the size of the cache exceed max cache size,
   remove least recently used key-value pair.
   If the key already exists, update the value.
 
- `get(key)`

   Returns the value of key-value pair of key: `key`.
     
- `del(key)`

   Removes the key-value pair of key: `key`.

- `reset()`

   Removes all key-value pair in the cache.
  
  
## Setting up and running the code
Make sure that [python3](https://www.python.org/downloads/)  is installed on the machine, and "LRUCache.py" & "main.py"  are downloaded and in the same directory.
### Running `main.py`

1. Open a terminal window and navigate to the `LRUCache` folder.
3. Run the following command: `python main.py`

### Expected Output
```
================ Adding Key & Values to Cache ================

================ Showing All Key & Values from Cache ================

OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])

================ Getting Specific Value ================

C

================ Putting Extra Value to Exceed Maximum Limit of Cache ================

D Added

================ Showing All New Key & Values from Cache ================

OrderedDict([(2, 'B'), (4, 'D'), (3, 'C')])

================ Delete A Value from Cache ================

True

================ Showing All New Key & Values from Cache ================

OrderedDict([(4, 'D'), (3, 'C')])

================ Resetting the Cache ================

================ Showing All New Key & Values from Cache ================

================ The End ================

```


