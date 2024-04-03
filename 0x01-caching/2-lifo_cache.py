#!/usr/bin/env python3
"""
Create a class that inherits from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Find the last key inserted into the cache."""
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD: {}".format(last_key))
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
