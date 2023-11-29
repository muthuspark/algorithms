import random

class CuckooHashTable:
    def __init__(self, size):
        self.size = size
        self.primary_table = [None] * size
        self.secondary_table = [None] * size
        self.MAX_RETRIES = 100  # Maximum retries to prevent infinite loops

    def hash1(self, key):
        """
        This method calculates the hash value for the given key using the modulo operator.
        It takes the key as input and returns the hash value.
        """
        return key % self.size

    def hash2(self, key):
        """
        The // operator in Python is called the floor division operator. 
        It performs division between two numbers and returns 
        the quotient rounded down to the nearest integer.

        For example, 7 // 2 will return 3, as the 
        quotient of dividing 7 by 2 is 3.5, and the // operator rounds it down to the nearest integer.
        """
        return (key // self.size) % self.size

    def display(self):
        # Join primary_table with | character
        print(f"\n||{'|'.join(str(x) for x in range(self.size))}|")
        print(f"|---{'|---' * self.size}| ")
        print(f"| Table 1 |{'|'.join(str(x) for x in self.primary_table)}|")
        print(f"| Table 2 |{'|'.join(str(x) for x in self.secondary_table)}|")

    def insert(self, key):
        if self.search(key):
            return  # Key already exists
        
        for _ in range(self.MAX_RETRIES):
            
            # Calculate the hash values for both the 
            # tables using their respective hash 
            # functions
            primary_hash_key = self.hash1(key)
            secondary_hash_key = self.hash2(key)

            print("hash1:", key, primary_hash_key)
            

            if self.primary_table[primary_hash_key] is None:
                # If the primary bucket is empty, 
                # then place the key in that bucket.
                self.primary_table[primary_hash_key] = key
                self.display()
                return
            
            print("hash2:", key, secondary_hash_key)

            # evict the key from the primary bucket
            # Swap key with existing key in table1
            temp = self.primary_table[primary_hash_key]
            self.primary_table[primary_hash_key] = key
            key = temp

            if self.secondary_table[secondary_hash_key] is None:
                self.secondary_table[secondary_hash_key] = key
                self.display()
                return
            

            temp = self.secondary_table[secondary_hash_key]
            self.secondary_table[secondary_hash_key] = key
            key = temp

        self.rehash()

    def search(self, key):
        return key in self.primary_table or key in self.secondary_table

    def delete(self, key):
        if key in self.primary_table:
            self.primary_table[self.primary_table.index(key)] = None
        elif key in self.secondary_table:
            self.secondary_table[self.secondary_table.index(key)] = None

    def rehash(self):
        print("Cycle is found. Rehashing..")
        # Double the size of tables
        self.size *= 2

        # Copy the keys from the two tables
        keys = [key for key in self.primary_table + self.secondary_table if key is not None]

        # empty the tables
        self.primary_table = [None] * self.size
        self.secondary_table = [None] * self.size
        
        # repopulate the keys.
        for key in keys:
            self.insert(key)

# Example Usage:
keys = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39, 6]
cuckoo = CuckooHashTable(len(keys))

for key in keys:
    cuckoo.insert(key)

print("Table 1:", cuckoo.primary_table)
print("Table 2:", cuckoo.secondary_table)