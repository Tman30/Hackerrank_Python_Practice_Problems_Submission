# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement,combinations
if __name__ == '__main__':
    string, r = input().split()
    output = list(combinations_with_replacement(string,int(r)))
    for i in range(len(output)):
        output[i] = sorted(output[i])
    output.sort()
    for i in output:
        print("".join(i))