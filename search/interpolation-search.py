#!/usr/bin/python
# -*- coding: utf-8 -*-
def interpolation_search(sorted_list, target):
    """
    Perform an interpolation search to find the target element in the given sorted list.

    Args:
        sorted_list (list): The sorted list to search in.
        target (int): The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    n = len(sorted_list)  # Length of the list
    low = 0  # Initialize the lower bound of the search range
    high = n - 1  # Initialize the upper bound of the search range

    while low <= high and sorted_list[low] <= target <= sorted_list[high]:
        # Estimate the position of the target using interpolation formula
        pos = low + ((target - sorted_list[low]) * (high - low) //
                     (sorted_list[high] - sorted_list[low]))
        if sorted_list[pos] == target:
            # Target element found at index pos
            return pos  
        elif sorted_list[pos] < target:
            # Target must be in the right half, update the lower bound
            low = pos + 1  
        else:
            # Target must be in the left half, update the upper bound
            high = pos - 1  

        print(sorted_list[pos], low, high, target)

    return -1  # Target element not found in the list


# Example usage:
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 26]
target = 13

result = interpolation_search(sorted_list, target)
if result != -1:
    print(f"Target element {target} found at index: {result}")
else:
    print(f"Target element {target} not found in the list.")
