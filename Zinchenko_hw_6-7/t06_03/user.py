class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * self.size
        self.num_elements = 0
        self.deleted = set()

    def _hash(self, key):
        """Хеш-функція для перетворення ключа на індекс"""
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def _probe(self, index, attempt):
        """Квадратичне пробування для вирішення колізій"""
        return (index + attempt ** 2) % self.size

    def _resize(self):
        """Збільшує розмір хеш-таблиці, коли вона заповнена більш ніж на 50%"""
        old_table = self.table
        self.size = self._next_prime(self.size * 2)
        self.table = [None] * self.size
        self.num_elements = 0

        for entry in old_table:
            if entry is not None and entry != "DELETED":
                author, titles = entry
                for title in titles:
                    self.insert(author, title)

    def _next_prime(self, n):
        """Знаходимо наступне просте число більше за n"""
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        while not is_prime(n):
            n += 1
        return n

    def insert(self, author, title):
        """Додає книгу до бібліотеки"""
        if self.num_elements >= self.size // 2:
            self._resize()

        index = self._hash(author)
        attempt = 0
        while self.table[index] is not None and self.table[index] != "DELETED":
            existing_author, titles = self.table[index]
            if existing_author == author:
                titles = tuple(titles)  
                if title not in titles:
                    titles = titles + (title,)  
                self.table[index] = (author, titles)  
                return
            attempt += 1
            index = self._probe(index, attempt)

        self.table[index] = (author, (title,))  
        self.num_elements += 1

    def find(self, author, title):
        """Перевіряє, чи є книга в бібліотеці"""
        index = self._hash(author)
        attempt = 0
        while self.table[index] is not None:
            if self.table[index] == "DELETED":
                attempt += 1
                index = self._probe(index, attempt)
                continue
            if self.table[index][0] == author and title in self.table[index][1]:
                return True
            attempt += 1
            index = self._probe(index, attempt)
        return False

    def delete(self, author, title):
        """Видаляє книгу з бібліотеки"""
        index = self._hash(author)
        attempt = 0
        while self.table[index] is not None:
            if self.table[index] == "DELETED":
                attempt += 1
                index = self._probe(index, attempt)
                continue
            if self.table[index][0] == author and title in self.table[index][1]:
                titles = list(self.table[index][1])
                titles.remove(title)  
                if not titles:
                    self.table[index] = "DELETED"  
                else:
                    self.table[index] = (author, tuple(titles))  
                self.num_elements -= 1
                self.deleted.add((author, title))  
                return
            attempt += 1
            index = self._probe(index, attempt)

    def findByAuthor(self, author):
        """Повертає список книг автора, відсортованих за алфавітом"""
        books = []
        index = self._hash(author)
        attempt = 0
        while self.table[index] is not None:
            if self.table[index] == "DELETED":
                attempt += 1
                index = self._probe(index, attempt)
                continue
            if self.table[index][0] == author:
                books.extend(self.table[index][1])  
            attempt += 1
            index = self._probe(index, attempt)
        return sorted(books)  

library_catalog = None

def init():
    global library_catalog
    library_catalog = HashTable(100)

def addBook(author, title):
    library_catalog.insert(author, title)

def find(author, title):
    return library_catalog.find(author, title)

def delete(author, title):
    library_catalog.delete(author, title)

def findByAuthor(author):
    return library_catalog.findByAuthor(author)

