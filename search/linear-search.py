#!/usr/bin/python
# -*- coding: utf-8 -*-
def linear_search(target, lst):
    """
    Perform a linear search to find the target element in the given list.

    Args:
        target (int): The element to search for.
        lst (list): The list to search in.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    for index, element in enumerate(lst):
        # print(f"Iteration {index} : is {element} == {target}? ")
        if element == target:
            return index
    return -1  # If the target element is not found, return -1

# Example usage:
my_list = [10, 7, 15, 22, 9, 13, 5]
target_element = 9

result = linear_search(target_element, my_list)
if result != -1:
    print(f"Target element {target_element} found at index: {result}")
else:
    print(f"Target element {target_element} not found in the list.")