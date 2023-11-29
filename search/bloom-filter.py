#!/usr/bin/python
# -*- coding: utf-8 -*-
import mmh3
import bitarray 

class BloomFilter:
    def __init__(self, size, hash_count):
        self.bit_array = bitarray.bitarray(size) # <1> Initialize a bit array of the given size
        self.bit_array.setall(0) # <2> Set all bits in the bit array to 0
        self.size = size # <3> Store the size of the bit array
        self.hash_count = hash_count # <4> Store the number of hash functions to use

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1  # <5> Set the bit at the calculated index to 1
            
    def lookup(self, item):
        # <6> Check each hash function
        for i in range(self.hash_count):
            # <7> Calculate the index using the hash function
            index = mmh3.hash(item, i) % self.size
            # <8> If the bit at the calculated index is 0, the item is not in the filter
            if self.bit_array[index] == 0:
                return False
        # <9> If all hash functions return 1, the item may be in the filter
        return True
        
bf = BloomFilter(100, 3)
bf.add("key1")
print(bf.lookup("key1")) # True
print(bf.lookup("key2")) # Could be False Positive!