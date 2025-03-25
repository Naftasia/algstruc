def main():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    numbers.sort(key=lambda x: (x % 10, x))
    print(" ".join(map(str, numbers)))

if __name__ == "__main__":
    main()
