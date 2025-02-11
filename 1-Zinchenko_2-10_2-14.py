"4 курс, математика, ммо, Зінченко А., 05.02.25"



# Завдання 2.10 (оптимізація ф-ї для покращення асимптотичної оцінки)

def f_1(n):
    return n * (n + 1) // 2         # O(n^2)

print("2.10:" , f_1(100))



# Завдання 2.14

def f_a(n):                     
    sum = 0                         # O(1)
    for i in range(n + 1):          # O(n)             
        sum += i                    # O(n)
    return sum                      # O(1)
print("2.14 (a):" , f_a(100))


def f_b(n):
    sum = 0                         # O(1)
    for i in range(n + 1):          # O(n)
        sum += i ** 2               # O(n)
    return sum                      # O(1)  
print("2.14 (b):" , f_b(100))


def f_c(a, n):
    sum = 0                         # O(1)
    elem = 1                        # O(1)
    for i in range(n + 1):          # O(n)
        sum += elem                 # O(n)
        elem *= a                   # O(n)
    return sum                      # O(1)
print("2.14 (c):" , f_c(2,5))


def f_d(i, n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        sum += i ** i               # O(n^2)
    return total                    # O(1)
print("2.14 (d):" , f_c(3, 2))


def f_e(n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        sum += 1 / (1 + i)          # O(n)
    return sum                      # O(1)
print("2.14 (e):" , f_e(6))


def f_f(n):
    sum = 0                         # O(1)
    fact = 1                        # O(1) 
    for i in range(1, n + 1):       # O(n)
        if i > 1:                   # O(n)
            fact *= i               # O(n)
        sum += 1 / (1 + fact)       # O(n)
    return sum                      # O(1)
print("2.14 (f):" , f_f(5))


def f_g(a, n):
    sum = 0                         # O(1)
    fact = 1                        # O(1)
    elem = 1                        # O(1)
    for i in range(1, n + 1):       # O(n)
        elem *= a                   # O(n)
        if i > 1:                   # O(n)
            fact *= i               # O(n)
        sum += elem / (1 + fact)    # O(n)
    return sum                      # O(1)
print("2.14 (g):" , f_g(2, 5))


def f_h(n, m):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        i_exp_m = i ** m            # O(nm)
        sum += 1 / (1 + i_exp_m)    # O(nm)
    return sum                      # O(1)
print("2.14 (h):" , f_h(5, 3))


def f_i(n):
    sum = 0                         # O(1)
    for i in range(1, n + 1):       # O(n)
        i_exp_i = i ** i            # O(n^2)
        sum += 1 / (1 + i_exp_i)    # O(n^2)
    return sum                      # O(1)
print("2.14 (i):" , f_i(5))















