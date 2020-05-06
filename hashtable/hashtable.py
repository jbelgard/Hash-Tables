class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return (f"(key = {self.key}, value = {self.value})")

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

        index = self.hash_index(key)
        if self.storage[index] is None:
            self.storage[index] = HashTableEntry(key=key, value=value)
        else:
            n = self.storage[index]
            while n.next is not None and n.key != key:
                n=n.next
            if n.key == key:
                n.value = value
            else:
                n.next = HashTableEntry(key=key, value=value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key=key)
        if self.storage[index] is None:
           return None
        else:
            
            #previous node
            p = None
            #current Node
            n = self.storage[index]
            #while n has a next node
            while n.next is not None:
                #if the current node key is the hashed key we are looking for, break the while loop
                if n.key == key:
                    break
                #else set previous to current node and current to next node
                else:
                    p = n
                    n = n.next

            #store the value so we can return it
            val = n.value
            #if p is not none then skip n
            if p is None:
                self.storage[index] = None
            #finally delete n
            else:
                p.next = n.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        index = self.hash_index(key=key)
        if self.storage[index] is not None:
            n = self.storage[index]
            while n.next is not None:
                if n.key == key:
                    return n.value
                n = n.next
            return n.value

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """

        key_values = {}
        for head in self.storage:
            if head is None:
                pass
            else:
                n=head
                key_values[n.key] = n.value
                while n.next is not None:
                    key_values[n.key] = n.value
                    n = n.next

        t_ht = HashTable(self.capacity*2)
        for key,value in key_values.items():
            t_ht.put(key, value)

        self.capacity *= 2
        self.storage = t_ht.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    
    print(ht.storage)

    ht.delete("line_1")

    print(ht.storage)
