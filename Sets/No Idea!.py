n,m = map(int,input().split())
arr = list(input().split())
A = set(input().split())
B = set(input().split())
happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -=1
print(happiness)