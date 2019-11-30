class HashTable:
    def __init__(self, init_size=10):
        self.buckets = [None for _ in range(init_size)]
        # self.len = 0

    def _bucket_index(self, key):
        return hash(key) % len(self.buckets)

    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        all_items = []
        for bucket in self.buckets:
            all_items.append(bucket)
        return all_items

    def length(self):
        return len(self.buckets)

    def contains(self):
        pass

    def get(self, key):
        pass

    def set(self, key, value):
        bucket_index = self._bucket_index(key)
        if self.buckets[bucket_index] is None:
            self.buckets[bucket_index] = (key, value)
        else:
            while self.buckets[bucket_index] is not None:
                if bucket_index == self.length() - 1:
                    for _ in range(self.length() * 2):
                        self.buckets.append(None)
                bucket_index += 1
            self.buckets[bucket_index] = (key, value)

    def delete(self, key):
        pass