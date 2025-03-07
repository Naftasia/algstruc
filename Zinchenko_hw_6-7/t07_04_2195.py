import re

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, word):
        hash_value = 0
        for char in word:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def insert(self, word):
        index = self._hash(word)
        if word not in self.table[index]:
            self.table[index].append(word)

    def contains(self, word):
        index = self._hash(word)
        return word in self.table[index]

N, M = map(int, input().split())

hash_table = HashTable(1000)

for _ in range(N):
    word = input().strip().lower()
    hash_table.insert(word)

text_words = set()

for _ in range(M):
    line = input().strip().lower()
    words = re.findall(r'\b[a-z]+\b', line)  
    text_words.update(words)

for word in text_words:
    if not hash_table.contains(word):
        print("Some words from the text are unknown.")
        break
else:
    for word in hash_table.table:
        for w in word:
            if w not in text_words:
                print("The usage of the vocabulary is not perfect.")
                break
        else:
            continue
        break
    else:
        print("Everything is going to be OK.")
