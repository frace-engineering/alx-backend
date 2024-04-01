#!/usr/bin/env python3
"""
Function that returns the start and end index of a page.
"""


def index_range(page, page_size) -> tuple:
    """
    Return the start and end index for a given page and page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int) The number of items per page.

    Return:
    - tuple: start index and end index for the given page.
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    return start_index, end_index
