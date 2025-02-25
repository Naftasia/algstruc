import math

def f(x, C):
    return x**2 + math.sqrt(x) - C
def bisection_method(C, tol=1e-7):
    left, right = 0, C
    if f(left, C) == 0:
        return left
    if f(right, C) == 0:
        return right
    
    while (right - left) / 2 > tol:
        mid = (left + right) / 2
        if f(mid, C) == 0:
            return mid
        elif f(mid, C) * f(left, C) < 0:
            right = mid
        else:
            left = mid
    
    return (left + right) / 2

def main():
    C = float(input())
    x = bisection_method(C)
    print(f"{x:.6f}")

if __name__ == "__main__":
    main()

" Корінь рівняння на відрізку [1.6, 3] : 2.278863 "
