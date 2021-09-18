from LRUCache import LRUCache


def main():
    # RUNNER
    # initializing our cache with the capacity of 3
    cache = LRUCache(3)
    print('================ Adding Key & Values to Cache ================')
    cache.put(1, 'A')
    cache.put(2, 'B')
    cache.put(3, 'C')

    print('================ Showing All Key & Values from Cache ================')
    print(cache.cache)

    print('================ Getting Specific Value ================')
    print(cache.get(3))

    print('================ Putting Extra Value to Exceed Maximum Limit of Cache ================')
    cache.put(4, 'D')
    print(cache.get(3) + ' Added')

    print('================ Showing All New Key & Values from Cache ================')
    print(cache.cache)

    print('================ Delete A Value from Cache ================')
    print(cache.delete(2))

    print('================ Showing All New Key & Values from Cache ================')
    print(cache.cache)

    print('================ Resetting the Cache ================')
    cache.reset()

    print('================ Showing All New Key & Values from Cache ================')
    print(cache.cache)

    print('================ The End ================')


if __name__ == "__main__":
    main()
