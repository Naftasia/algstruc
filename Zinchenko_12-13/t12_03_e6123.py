class Node:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self.count += 1
        print("ok")

    def pop(self):
        if self.top is None:
            print("error")
        else:
            print(self.top.value)
            self.top = self.top.prev
            self.count -= 1

    def back(self):
        if self.top is None:
            print("error")
        else:
            print(self.top.value)

    def size(self):
        print(self.count)

    def clear(self):
        self.top = None
        self.count = 0
        print("ok")

def stack_machine():
    stack = Stack()

    while True:
        try:
            line = input()
        except EOFError:
            break

        line = line.strip()
        if line.startswith("push"):
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                arg = parts[1].strip()
                if arg.isdigit():
                    stack.push(int(arg))
                else:
                    print("error")
            else:
                print("error")

        elif line == "pop":
            stack.pop()

        elif line == "back":
            stack.back()

        elif line == "size":
            stack.size()

        elif line == "clear":
            stack.clear()

        elif line == "exit":
            print("bye")
            break

        else:
            print("error")

stack_machine()
