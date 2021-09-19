import unittest
from LRUCache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_put(self):
        cache = LRUCache(3)
        self.assertIsNone(cache.put(1, 'A'))
        self.assertIsNone(cache.put('One', 'A'))
        self.assertIsNone(cache.put(2, 'B'))
        self.assertIsNone(cache.put(3, 'C'))
        self.assertIsNotNone(cache.get(3))
        self.assertIsNone(cache.put(4, 'D'))
        self.assertTrue(cache.get(4))
        self.assertIsNotNone(cache.get("A"))
        self.assertTrue(cache.get(2))
        self.assertTrue(cache.get(1))
        self.assertTrue(cache.delete(3))
        self.assertFalse(cache.delete("D"))
        self.assertTrue(cache.reset())


if __name__ == '__main__':
    unittest.main()
