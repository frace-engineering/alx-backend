#!/usr/bin/env python3
"""
Function that returns the start and end index of a page.
"""
import csv
import math
from typing import Tuple, List


def index_range(page, page_size) -> tuple:
    """
    Return the start and end index for a given page and page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int) The number of items per page.

    Return:
    - tuple: start index and end index for the given page.
    """
    start_index = page_size * (page)
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page must be int & > 0"
        assert isinstance(page_size, int) and page_size > 0, "Size must be int"
        "and greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index + 1]
