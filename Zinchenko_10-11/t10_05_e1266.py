def process_input(data):
    results = []
    for line in data:
        numbers = list(map(int, line.split()))
        N = numbers[0] 
        s = numbers[1]
        tracks = numbers[2:]  
        dp = [False] * (N + 1)
        dp[0] = True 

        for track in tracks:
            for time in range(N, track - 1, -1):
                if dp[time - track]:
                    dp[time] = True
        
        for max_time in range(N, -1, -1):
            if dp[max_time]:
                results.append(f"sum:{max_time}")
                break
    
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    results = process_input(data)
  
    for result in results:
        print(result)

main()
