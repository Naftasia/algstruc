
def check_butterflies_in_collection():
    n = int(input())
    collection = set(map(int, input().split())) 
    m = int(input())
    queries = list(map(int, input().split()))
    
    for q in queries:
        if q in collection:  
            print("YES")
        else:
            print("NO")
            
check_butterflies_in_collection()
