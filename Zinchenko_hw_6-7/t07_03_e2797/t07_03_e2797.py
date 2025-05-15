def is_prime_number(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

class ContactStorage:
    def __init__(self, initial_capacity=13):
        self.capacity = initial_capacity
        self.entries = 0
        self.data = [None] * self.capacity

    def _hash_function(self, value):
        return value % self.capacity

    def _expand(self):
        previous_data = self.data
        updated_capacity = self.capacity * 2 + 1

        while not is_prime_number(updated_capacity):
            updated_capacity += 2

        self.capacity = updated_capacity
        self.data = [None] * self.capacity
        self.entries = 0

        for item in previous_data:
            if item is not None:
                self.insert(item)

    def insert(self, value):
        if self.entries >= self.capacity * 0.7:
            self._expand()

        position = self._hash_function(value)
        initial_position = position

        while self.data[position] is not None:
            if self.data[position] == value:
                return
            position = (position + 1) % self.capacity
            if position == initial_position:
                return

        self.data[position] = value
        self.entries += 1

def main():
    total = int(input())
    call_list = list(map(int, input().split()))
    
    contacts = ContactStorage()

    for phone in call_list:
        contacts.insert(phone)

    print(contacts.entries)

if __name__ == "__main__":
    main()
