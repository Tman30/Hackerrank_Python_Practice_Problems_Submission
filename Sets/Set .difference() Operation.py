import os
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'],'w')
    
    n_english = int(input())
    roll_english = set(list(map(int,input().split())))
    n_french = int(input())
    roll_french = set(list(map(int,input().split())))
    roll_only_eng = roll_english.difference(roll_french)
    result = len(roll_only_eng)
    fptr.write(str(result))
    fptr.close()