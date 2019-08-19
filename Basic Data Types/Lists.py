def insert(x):
   return arr.insert(x[0],x[1])
def remove(x):
    return arr.remove(x[0])
def prnt(x):
    print(arr)
def append(x):
    return arr.append(x[0])
def sort(x):
    return arr.sort()
def pop(x):
    return arr.pop()
def reverse(x):
    return arr.reverse()
actions = {'insert': insert, 'remove': remove, 'print': prnt, 'append': append, 'sort': sort, 'pop': pop,'reverse': reverse}
arr = []
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        name, *inp = input().split()
        var = list(map(int,inp))
        actions[name].__call__(var)