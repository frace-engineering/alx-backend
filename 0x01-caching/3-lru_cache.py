#!/usr/bin/env python3
"""
Create a class that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize LRUCache
        """
        super().__init__()
        """ Keeps track of the order of keys accessed"""
        self.access_tracker = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Find the least recently used key."""
                lru_key = self.access_tracker.pop(0)
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.access_tracker.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is not None:
            """Update access_tracker to reflect recent access."""
            if key in self.access_tracker:
                self.access_tracker.remove(key)
            self.access_tracker.append(key)

            return self.cache_data.get(key)
        return None
