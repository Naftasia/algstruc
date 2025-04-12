def is_valid_bracket_sequence(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "no"
            stack.pop()
    
    return "yes" if not stack else "no"

if __name__ == "__main__":
    sequence = input().strip()
    print(is_valid_bracket_sequence(sequence))
