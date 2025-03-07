def get_hash(key, size):
    return key % size

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  
    
    def insert(self, key):
        hash_index = get_hash(key, self.size)
        if key not in self.table[hash_index]:
            self.table[hash_index].append(key)
    
    def get_unique_count(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)  
        return count

N = int(input())  
phones = list(map(int, input().split()))
hash_table_size = 10007  
hash_table = HashTable(hash_table_size)

for phone in phones:
    hash_table.insert(phone)

print(hash_table.get_unique_count())
