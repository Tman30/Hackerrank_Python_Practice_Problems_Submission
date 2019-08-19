# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    string,r = input().split()
    for j in range(int(r)):
        for i in combinations(sorted(string),int(j+1)):
            print("".join(i))