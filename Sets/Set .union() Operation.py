import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    n_english = int(input())
    roll_english = set(list(map(int,input().split())))
    n_french = int(input())
    roll_french = set(list(map(int,input().split())))
    print(roll_english,roll_french)
    roll_total = roll_english.union(roll_french)
    result = len(roll_total)
    fptr.write(str(result))
    fptr.close()