import sys

sys.set_int_max_str_digits(1000000)

def karatsuba(A, B):
    if A == 0 or B == 0:
        return 0

    A_str = str(A)
    B_str = str(B)

    if len(A_str) == 1 or len(B_str) == 1:
        return A * B

    n = max(len(A_str), len(B_str))
    half = n // 2

    A_high = A // 10**half
    A_low = A % 10**half
    B_high = B // 10**half
    B_low = B % 10**half

    z2 = karatsuba(A_high, B_high)
    z0 = karatsuba(A_low, B_low)
    z1 = karatsuba(A_high + A_low, B_high + B_low) - z2 - z0

    return z2 * 10**(2 * half) + z1 * 10**half + z0

A, B = map(int, input().split())
result = karatsuba(A, B)
print(result)
