if __name__ == '__main__':
    m = int(input())
    set1 = set(map(int,input().split()))
    n = int(input())
    set2 = set(map(int,input().split()))
    set3 = set1 ^ set2
    print(*(sorted(list(set3))), sep = "\n")  