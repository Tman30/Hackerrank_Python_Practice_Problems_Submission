if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    y = max(arr)
    while(y == max(arr)):
        arr.remove(y)
    print(max(arr))