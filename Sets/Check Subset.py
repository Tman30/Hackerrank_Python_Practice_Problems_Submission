N = int(input())
for _ in range(N):
    n_A = int(input())
    A = set(list(map(int,input().split())))
    n_B = int(input())
    B = set(list(map(int,input().split())))
    C = A.difference(B)
    if len(C):
        print("False")
    else:
        print("True")