# Complete the solve function below.
def solve(s):
    return("".join(s[i].upper() if (s[i].isalpha() and s[i].islower() and (s[i-1]==" " or i == 0)) else s[i] for i in range(len(s)) ))