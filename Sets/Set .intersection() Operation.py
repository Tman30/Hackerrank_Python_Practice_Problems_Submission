import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    
    n_english = int(input())
    roll_english = set(list(map(int,input().split())))
    n_french = int(input())
    roll_french = set(list(map(int,input().split())))
    roll_both = roll_english.intersection(roll_french)
    result = len(roll_both)
    fptr.write(str(result))
    fptr.close()