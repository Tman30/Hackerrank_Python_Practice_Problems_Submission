# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n,m = list(map(int,input().split()))
    c = ".|."
    l = int((n-1)/2)
    p = int((m-3)/2)
    for i in range(l):
        print((c*i).rjust(p,"-")+c+(c*i).ljust(p,"-"))
    print("WELCOME".center(m,"-"))
    for i in range(l):
        print((c*(l-i-1)).rjust(p,"-")+c+(c*(l-i-1)).ljust(p,"-"))