#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib

class BloomFilter:
    """
    This class represents a Bloom filter.
    
    Attributes:
        bit_array (list): The bit array used to store the filter.
        num_hash_functions (int): The number of hash functions to use.
    """
    def __init__(self, size, num_hash_functions):
        self.bit_array = [0] * size
        self.num_hash_functions = num_hash_functions

    def add(self, element):
        # Iterate through the hash functions
        for i in range(self.num_hash_functions):
            # Calculate the hash value for the element
            hash_value = hashlib.md5(element.encode('utf-8')).hexdigest()[0:8]
            # Calculate the index in the bit array
            index = int(hash_value, 16) % len(self.bit_array)
            # Set the bit at the index to 1
            self.bit_array[index] = 1

    def contains(self, element):
        # Iterate through the hash functions
        for i in range(self.num_hash_functions):
            # Calculate the hash value for the element
            hash_value = hashlib.md5(element.encode('utf-8')).hexdigest()[0:8]
            # Calculate the index in the bit array
            index = int(hash_value, 16) % len(self.bit_array)
            # Check if the bit at the index is 0
            if self.bit_array[index] == 0:
                return False
        return True

# Create a Bloom filter with 1000 bits and 10 hash functions.
bloom_filter = BloomFilter(10, 3)

# Add some elements to the Bloom filter.
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# Test whether an element is a member of the Bloom filter.
print("apple", bloom_filter.contains("apple")) # True
print("grape", bloom_filter.contains("grape")) # False