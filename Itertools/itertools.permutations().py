# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
if __name__ == '__main__':
    string,k = input().split()
    for i in permutations(sorted(string),int(k)):
        print("".join(i))