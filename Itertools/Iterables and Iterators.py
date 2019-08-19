# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
if __name__ == '__main__':
    count = 0
    N = int(input())
    string_list = list(input().split())
    K = int(input())
    comb_list = list(combinations(string_list,K))
    for i in comb_list:
        if 'a' in i:
            count +=1
    print('{0:.{1}f}'.format(count/len(comb_list),3))