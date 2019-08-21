A = set(list(map(int,input().split())))
n = int(input())
output = True
for _ in range(n):
    B = set(list(map(int,input().split())))
    C = B.difference(A)
    D = A.difference(B)
    if len(C):
        output = False
        break
    elif not len(D):
        output = False
        break
print(output)