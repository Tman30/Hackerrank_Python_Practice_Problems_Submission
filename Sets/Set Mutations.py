n = int(input())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command,value = input().split()
    B = set(list(map(int,input().split())))
    if command == "intersection_update":
        A.intersection_update(B)
    elif command == "update":
        A.update(B)
    elif command == "symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif command == "difference_update":
        A.difference_update(B)
print(sum(list(A)))