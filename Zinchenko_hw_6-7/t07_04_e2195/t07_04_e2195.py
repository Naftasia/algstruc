class SimpleHashTable:
    def __init__(self, initial_capacity=13):
        self.capacity = initial_capacity
        self.size = 0
        self.data = [None] * self.capacity

    def _calculate_hash(self, key):
        return sum(ord(char) for char in key) % self.capacity

    def _is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def _resize(self):
        old_data = self.data
        new_capacity = self.capacity * 2 + 1

        while not self._is_prime(new_capacity):
            new_capacity += 2

        self.capacity = new_capacity
        self.data = [None] * self.capacity
        self.size = 0

        for entry in old_data:
            if entry is not None:
                self._insert(entry)

    def _insert(self, key):
        if self.size >= self.capacity * 0.7:
            self._resize()

        index = self._calculate_hash(key)
        initial_index = index

        while self.data[index] is not None:
            if self.data[index] == key:
                return
            index = (index + 1) % self.capacity
            if index == initial_index:
                return

        self.data[index] = key
        self.size += 1

    def contains(self, key):
        index = self._calculate_hash(key)
        initial_index = index

        while self.data[index] is not None:
            if self.data[index] == key:
                return True
            index = (index + 1) % self.capacity
            if index == initial_index:
                return False
        return False


def process_text_line(line, table):
    word = ""
    for char in line:
        if 'a' <= char <= 'z':
            word += char
        elif word:
            table._insert(word)
            word = ""
    if word:
        table._insert(word)


def main():
    dict_size, text_lines = map(int, input().split())

    dictionary_table = SimpleHashTable()
    text_table = SimpleHashTable()

    for _ in range(dict_size):
        word = input().strip().lower()
        dictionary_table._insert(word)

    for _ in range(text_lines):
        line = input().strip().lower()
        process_text_line(line, text_table)

    missing_in_dict = False
    missing_in_text = False

    for word in text_table.data:
        if word is not None and not dictionary_table.contains(word):
            missing_in_dict = True
            break

    if not missing_in_dict:
        for word in dictionary_table.data:
            if word is not None and not text_table.contains(word):
                missing_in_text = True
                break

    if missing_in_dict:
        print("Some words from the text are unknown.")
    elif missing_in_text:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == "__main__":
    main()
