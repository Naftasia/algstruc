
def f(x):
    return x**3 + 4*x**2 + x - 6


def bisection_method(a, b, tol=1e-7):
    if f(a) * f(b) > 0:
        print("Корінь не можна знайти в заданому відрізку, оскільки функція не змінює знак.")
        return None
    
    while (b - a) / 2 > tol:
        mid = (a + b) / 2
        if f(mid) == 0:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    
    return (a + b) / 2

def main():
    a, b = 0, 2
    root = bisection_method(a, b)
    
    if root is not None:
        print(f"Корінь рівняння на відрізку [{a}, {b}] : {root:.6f}")

if __name__ == "__main__":
    main()

" Корінь рівняння на відрізку [0, 2] : 1.000000 " 
