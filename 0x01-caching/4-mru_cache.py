#!/usr/bin/env python3
"""
Create a class that inherits from BaseCaching and is a caching system.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize MRUCache
        """
        super().__init__()
        """Keeps track of the order of keys accessed."""
        self.access_tracker = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Find the most recently used key."""
                mru_key = self.access_tracker.pop()
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]
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
