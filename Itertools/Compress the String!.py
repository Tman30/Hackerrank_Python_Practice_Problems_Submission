# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
if __name__ == '__main__':
    for X,c in groupby(input()):
        print("({0}, {1})".format(len(list(c)),int(X)),end = " ")