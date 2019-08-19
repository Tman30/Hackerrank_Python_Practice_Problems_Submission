# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
if __name__ == '__main__':
    s   = 0
    all_list = []
    k,m = map(int,input().split())
    for _ in range(int(k)):
        n,*elem = map(int,input().split())
        all_list.append(tuple(map(lambda x: x ** 2, list(elem))))
    
    for i in list(product(*all_list)):
        if s < sum(i)%m:
            s = sum(i)%m
    print(s)