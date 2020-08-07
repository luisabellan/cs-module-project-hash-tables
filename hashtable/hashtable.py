class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [[] for _ in range(self.capacity)]
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
       Returns: The FNV-1 hash of a given string. 
        """
        #Constants
        prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1 Hash Function
        my_hash = offset_basis
        for char in key:
            my_hash = my_hash ^ ord(char)
            my_hash = my_hash * prime
            my_hash &= 0xffffffffffffffff
        return my_hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        prime = 5381
        for c in key:
            my_hash = (prime * 33) + ord(c)
            my_hash &= 0xffffffff
        return my_hash
    


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #if self.get(key) == None:
        self.hash_table[self.hash_index(key)] = (key,value)
        """
        - fix this to pass test_hash_table_pution_overwrites_correctly case in test function in test_hashtable_no_collisions.py  -
         else:
            position = self.hash_index(key)
            self.delete(position)
            self.hash_table[self.hash_index(key)].insert(position,(key,value)) """

        
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #self.hash_table[self.hash_index(key)].append((key,None))
        del self.hash_table[self.hash_index(key)]



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        
        
        # self.hash_table = [] * MIN_CAPACITY
        # self.hash_index(key)
        #for k,v in self.hash_table[self.hash_index(key)]:
        #    if k == key:
        #        return v
        #    return None 
        
        if self.hash_table[self.hash_index(key)]: 
            [k,v] = self.hash_table[self.hash_index(key)]
            return v
        return None

       



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
