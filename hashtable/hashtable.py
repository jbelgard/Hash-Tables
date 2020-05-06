class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """

        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffffffffffff

        return total

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        total = 0
        for b in key.encode():
            total += b
            total &= 0xffffffff

        return total

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

        targ = self.hash_index(key)
        if self.head is None:
            self.head = HashTableEntry(key = targ, value = value)
        else:
            n = self.head
            while n.next is not None and n.key is not targ:
                n = n.next
            n.next = HashTableEntry(key = targ, value = value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        if self.head is None:
            return "Key Not Found"
        else:
            targ = self.hash_index(key=key)
            #previous node
            p = None
            #current Node
            n = self.head
            #while n has a next node
            while n.next is not None:
                #if the current node key is the hashed key we are looking for, break the while loop
                if n.key == targ:
                    break
                #else set previous to current node and current to next node
                else:
                    p = n
                    n = n.next

            #store the value so we can return it
            val = n.value
            #if p is not none then skip n
            if p is not None:
                p.next = n.next
            #finally delete n
            del(n)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        targ = self.hash_index(key=key)
        if self.head is not None:
            n = self.head
            while n.next is not None:
                if n.key == targ:
                    return n.value
                n = n.next

        return "Key not Found"

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
