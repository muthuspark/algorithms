#!/usr/bin/python
# -*- coding: utf-8 -*-
def binary_search(sorted_list, target):
    """
    Perform a binary search to find the target element in the given sorted list.

    Args:
        sorted_list (list): The sorted list to search in.
        target (int): The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            # Target element found at index mid
            return mid
        elif sorted_list[mid] < target:
            # Search the right half
            left = mid + 1
        else:
            # Search the left half
            right = mid - 1
    # Target element not found in the list
    return -1


# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 13

result = binary_search(sorted_list, target)
if result != -1:
    print(
        f"Target element {target} found at index: {result}")
else:
    print(f"Target element {target} not found in the list.")
