if __name__ == '__main__':
    N = int(raw_input().strip())
    stamp_set  = []
    for _ in range(N):
        stamp = raw_input().strip()
        stamp_set.append(stamp)
    print(len(set(stamp_set)))