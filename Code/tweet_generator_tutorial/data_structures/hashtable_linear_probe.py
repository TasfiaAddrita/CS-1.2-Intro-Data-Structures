class HashTableIterator:
    def __init__(self, hashtable):
        self._hashtable = hashtable.buckets
        self._index = 0
    
    def __next__(self):
        if self._index < len(self._hashtable)-1:
            self._index += 1
            return self._hashtable[self._index]
        raise StopIteration

class HashTable:
    def __init__(self, init_size=10):
        if init_size <= 4:
            raise ValueError("Please enter a size above 4.")
        else:
            self.buckets = [None for _ in range(init_size)]
        self.MAX_CAPACITY = 0.75 # grow the array if it's 75% full

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def __iter__(self):
        return HashTableIterator(self)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def _bucket_index(self, key):
        return hash(key) % len(self.buckets)

    def keys(self):
        all_keys = []
        for item in self.items():
            all_keys.append(item[0])
        return all_keys

    def values(self):
        all_values = []
        for item in self.items():
            all_values.append(item[1])
        return all_values

    def items(self):
        return [bucket for bucket in self.buckets if bucket is not None]

    # number of key-value pairs in hashtable
    def length(self):
        return len(self.items())

    def resize(self):
        items = self.items()
        self.buckets = [None for _ in range(len(self.buckets) * 2)]
        index = 0
        for item in items:
            self.set(item[0], item[1])

    def contains(self, key):
        bucket_index = self._bucket_index(key)
        turns = 0
        while self.buckets[bucket_index] != key and turns < len(self.buckets):
            if self.buckets[bucket_index] is not None and self.buckets[bucket_index][0] == key:
                return bucket_index
            else:
                if bucket_index == len(self.buckets)-1:
                    bucket_index = 0
                else:
                    bucket_index += 1
                turns += 1
        return False
    
    def get(self, key):
        bucket_index = self.contains(key)
        if bucket_index:
            return self.buckets[bucket_index][1]
        raise ValueError('Key not found')

    def set(self, key, value):
        if self.length() == 0:
            bucket_index = self._bucket_index(key)
            self.buckets[bucket_index] = (key, value)
        else:
            bucket_index = self.contains(key)
            print(bucket_index)
            if bucket_index == False:
                while self.buckets[bucket_index] is not None:
                    if bucket_index == len(self.buckets)-1:
                        bucket_index = 0
                    else:
                        bucket_index += 1
            self.buckets[bucket_index] = (key, value)
        if self.length() / len(self.buckets) > self.MAX_CAPACITY:
            self.resize()

    def delete(self, key):
        bucket_index = self.contains(key)
        if bucket_index:
            self.buckets[bucket_index] = None

if __name__ == "__main__":

    ht = HashTable(5)

    keys = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'lilac', 'periwinkle']
    value = 0

    for key in keys:
        ht.set(key, value)
        # print('num items', ht.length())
        # print('num buckets', len(ht.buckets))
        # print(ht.buckets)
        # print()
        value += 1
    
    # print(ht)

    # for bucket in ht:
    #     print(bucket)

    ht['olive'] = 3
    print(ht)

    ht['green'] = 90
    print(ht)

    # print(ht.buckets)
    # print(ht.get('red'))

    # print(ht.items())
    # print(ht.keys())
    # print(ht.values())

    # print(ht.get('green'))
    # print(ht.get('brown'))

    # print(ht.items())
    # ht.delete('orange')
    # print(ht.items())

    

    
