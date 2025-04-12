def check_permutation(n, target):
    station = []
    current = 1 

    for wagon in target:
        while current <= n and (not station or station[-1] != wagon):
            station.append(current)
            current += 1

        if station and station[-1] == wagon:
            station.pop()
        else:
            return "No"
    
    return "Yes"

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    index = 0

    while True:
        n = int(input_lines[index])
        if n == 0:
            break
        index += 1

        while True:
            line = input_lines[index]
            index += 1
            if line == "0":
                print()
                break
            target = list(map(int, line.strip().split()))
            print(check_permutation(n, target))

if __name__ == "__main__":
    main()
