if __name__ == '__main__':
    result = [False,False,False,False,False]
    s = input()
    for i in s:
        if i.isalnum():
            result[0] = True
        if i.isalpha():
            result[1] = True
        if i.isdigit():
            result[2] = True
        if i.islower():
            result[3] = True
        if i.isupper():
            result[4] = True
    for i in range(5):
        print(result[i])