def prefix_to_infix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    associative = {'+': True, '-': False, '*': True, '/': False}
    stack = []

    for token in reversed(expr):
        if token.isalpha():
            stack.append((token, None))
        else:
            left_expr, left_prec = stack.pop()
            right_expr, right_prec = stack.pop()
            curr_prec = precedence[token]
            is_assoc = associative[token]

            if left_prec is not None and left_prec < curr_prec:
                left_expr = f'({left_expr})'

            if right_prec is not None:
                if right_prec < curr_prec:
                    right_expr = f'({right_expr})'
                elif right_prec == curr_prec and not is_assoc:
                    right_expr = f'({right_expr})'

            combined = f'{left_expr}{token}{right_expr}'
            stack.append((combined, curr_prec))

    return stack[0][0]

with open('input.txt') as f:
    expr = f.read().strip()

with open('output.txt', 'w') as f:
    f.write(prefix_to_infix(expr))
