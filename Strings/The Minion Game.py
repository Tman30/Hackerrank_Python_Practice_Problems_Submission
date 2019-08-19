def minion_game(string):
    vowel = 'AEIOU'
    stuart,kevin = 0,0
    for i in range(len(string)):
        if string[i] in vowel:
            kevin += len(string)-i
        else:    
            stuart += len(string)-i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart>kevin:
        print("Stuart",stuart)
    else:
        print("Draw")