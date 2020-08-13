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

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity =capacity
        self.max_load_factor = 0.7
        self.size = 0
        self.buckets = [None]*self.capacity
        self.keyslist = []
        


    def get_num_slots(self):
        """
        Return the length or size of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.buckets / self.capacity



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

    def rehash_if_needed(self):
        if self.size >= self.max_load_factor * self.get_num_slots():
            self.resize(self.get_num_slots() * 2)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #if self.get(key) == None:
        
        
        # 1. Increment size
        self.size += 1

        # 2. Compute index of key
        index = self.hash_index(key)
        #self.buckets[index] = (key,value)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        if node == None: # we only need this if we don't want to be able to overwrite it
            # Create node, add it, return
            self.size += 1
            node.key = key
            node.value = value
            self.rehash_if_needed()
            return 
        # TODO fix this
        else:

            self.size += 1
            node.next.key = key
            node.next.value = value
            self.rehash_if_needed()
            return 

		# 4. Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value
        prev.next = HashTableEntry(key, value)



        """
        - fix this to pass test_buckets_pution_overwrites_correctly case in test function in test_hashtable_no_collisions.py  -
         else:
            position = self.hash_index(key)
            self.delete(position)
            self.buckets[self.hash_index(key)].insert(position,(key,value)) """

        
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #self.buckets[self.hash_index(key)].append((key,None))

        # del self.buckets[self.hash_index(key)]

        	# 1. Compute hash
        index = self.hash_index(key)
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
		# Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
			# 4. The key was found.
            self.size -= 1
            result = node.value
			# Delete this element in linked list
            if prev is None:
                self.buckets[index] = node.next # May be None, or the next match
            else:
                prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result
            return result



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        
        
        # self.buckets = [] * MIN_CAPACITY
        # self.hash_index(key)
        #for k,v in self.buckets[self.hash_index(key)]:
        #    if k == key:
        #        return v
        #    return None 
        
        #if self.buckets[self.hash_index(key)]: 
        #    [k,v] = self.buckets[self.hash_index(key)]
        #    return v
        #return None


        # 1. Compute hash
        index = self.hash_index(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value
            
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
         # Create new hashmap with new capacity 
        new_hashtable = HashTable(new_capacity)
        # Insert all the keys in the new hashmap
        for key in self.keyslist:
            value = self.get(key)
            new_hashtable.put(key, value)

        # Copy all the fields of the new hashmap to this hashmap
        self.capacity = new_hashtable.capacity
        self.max_load_factor = new_hashtable.max_load_factor
        self.size = new_hashtable.size
        self.buckets = new_hashtable.buckets
        self.keyslist = new_hashtable.keyslist



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
