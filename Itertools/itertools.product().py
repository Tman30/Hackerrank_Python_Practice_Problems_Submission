# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(product(A,B))
    C.sort()
    for i in C:
        print(i, end=" ")