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
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.item_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
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
        # number of items / num_slots
        # Your code here
        return self.item_count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # 64-bit constants
        FNV_offset_basis_64 = 0xcbf29ce484222325
        FNV_prime_64 = 0x100000001b3

        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        hash = FNV_offset_basis_64

        for b in str_key:
            hash *= FNV_prime_64
            hash ^= b
            hash &= 0xffffffffffffffff  # 64-bit hash

        return hash
        # $%$End
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # $%$Start
        # Cast the key to a string and get bytes
        str_key = str(key).encode()

        # Start from an arbitrary large prime
        hash_value = 5381

        # Bit-shift and sum value for each character
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff  # DJB2 is a 32-bit hash, only keep 32 bits

        return hash_value
        # $%$End


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        # no collision 
        if self.storage[index] is None:
            self.item_count += 1
            self.storage[index] = HashTableEntry(key, value)
        else: 
            # We have a collision
            # check for duplicate key
            # get the current head value
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    # we simply need to replace the value, and return
                    current_node.value = value
                    return
                current_node = current_node.next

            # No duplicate key found, add new entry to head
            head = self.storage[index]
            # create a new HashTableEntry which will  be the new head
            new_head = HashTableEntry(key, value)
            new_head.next = head
            self.item_count += 1
            self.storage[index] = new_head
        current_load_factor = self.get_load_factor()
        if current_load_factor > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # get the index for the linked list
        index = self.hash_index(key)
        # find and delete the node in the specific linked list
        current_node = self.storage[index]
        # if the head is the node to delete, handle that case
        if current_node.key == key:
            self.item_count -= 1
            self.storage[index] = current_node.next

            if self.get_load_factor() < 0.2:
                new_capacity = self.capacity // 2
                if new_capacity < MIN_CAPACITY:
                    new_capacity = MIN_CAPACITY
                self.resize(new_capacity)

            return 
        prev_node = None
        while current_node:
            if current_node.key == key:
                # delete the node from the linked list here
                self.item_count -= 1
                prev_node.next = current_node.next

                if self.get_load_factor() < 0.2:
                    new_capacity = self.capacity // 2
                    if new_capacity < MIN_CAPACITY:
                        new_capacity = MIN_CAPACITY
                    self.resize(new_capacity)

                return
            prev_node = current_node
            current_node = current_node.next
        print(f"Warning {key} not found in Hash Table")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.storage[index]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next



    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_storage = self.storage
        # Resetting the hash table with new capacity
        self.storage = [None] * new_capacity
        self.capacity = new_capacity
        self.item_count = 0

        # go through each item in old_storage
        for head in old_storage:
            # go through each item in the linked list and re-hash
            current_node = head
            while current_node:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next
        



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