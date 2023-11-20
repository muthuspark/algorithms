import hashlib

class CuckooFilter:
    def __init__(self, size, max_kicks):
        self.size = size  # Size of the filter
        self.max_kicks = max_kicks  # Max number of displacement attempts
        self.bit_array = [0] * size  # Bit array for storing fingerprints

    def hash_func(self, item):
        # Use hashlib's SHA256 hashing function
        return int(hashlib.sha256(item.encode()).hexdigest(), 16) % self.size

    def get_fingerprint(self, item):
        # Get the fingerprint of the item using its hash value
        return self.hash_func(item)

    def get_alternate_index(self, index, fingerprint):
        # Compute an alternate index based on the fingerprint
        return (index ^ self.hash_func(str(fingerprint))) % self.size

    def insert(self, item):
        fingerprint = self.get_fingerprint(item)
        index1 = self.hash_func(item)
        index2 = self.get_alternate_index(index1, fingerprint)

        if self.bit_array[index1] == 0:
            self.bit_array[index1] = fingerprint
            return True
        elif self.bit_array[index2] == 0:
            self.bit_array[index2] = fingerprint
            return True
        else:
            # Perform cuckoo hashing
            for _ in range(self.max_kicks):
                if self.bit_array[index1] == 0:
                    self.bit_array[index1] = fingerprint
                    return True
                elif self.bit_array[index2] == 0:
                    self.bit_array[index2] = fingerprint
                    return True
                else:
                    # Randomly choose an index to kick out its fingerprint
                    idx_to_kick = index1 if (hash(item) % 2 == 0) else index2
                    old_fingerprint = self.bit_array[idx_to_kick]
                    self.bit_array[idx_to_kick] = fingerprint
                    fingerprint = old_fingerprint
                    index1 = idx_to_kick
                    index2 = self.get_alternate_index(index1, fingerprint)
        return False

    def contains(self, item):
        fingerprint = self.get_fingerprint(item)
        index1 = self.hash_func(item)
        index2 = self.get_alternate_index(index1, fingerprint)

        if self.bit_array[index1] == fingerprint or self.bit_array[index2] == fingerprint:
            return True
        return False

    def delete(self, item):
        fingerprint = self.get_fingerprint(item)
        index1 = self.hash_func(item)
        index2 = self.get_alternate_index(index1, fingerprint)

        if self.bit_array[index1] == fingerprint:
            self.bit_array[index1] = 0
            return True
        elif self.bit_array[index2] == fingerprint:
            self.bit_array[index2] = 0
            return True
        return False

# Example usage:
cuckoo = CuckooFilter(size=100, max_kicks=500)

# Insert elements
cuckoo.insert("apple")
cuckoo.insert("orange")
cuckoo.insert("banana")

# Check if elements are present
print(cuckoo.contains("apple"))  # Output: True
print(cuckoo.contains("grape"))  # Output: False

# Delete an element
cuckoo.delete("orange")

# Check if the deleted element is present
print(cuckoo.contains("orange"))  # Output: False