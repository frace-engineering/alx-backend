#!/usr/bin/env python3

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the first key inserted into the cache
                first_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
