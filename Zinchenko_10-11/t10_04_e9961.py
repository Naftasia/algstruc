def generate_permutations(n, k, current_permutation, used):
    if len(current_permutation) == k:
        print(" ".join(map(str, current_permutation)))
        return

    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            generate_permutations(n, k, current_permutation + [i], used)
            used[i] = False 

def main():
    n, k = map(int, input().split())
    used = [False] * (n + 1)
    generate_permutations(n, k, [], used)

main()
