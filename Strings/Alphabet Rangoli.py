def print_rangoli(size):
    width = size*4 - 3
    for i in range(1-size,size):
        string = chr(97+abs(i))
        string2 = "".join(chr(97+size-j)+'-' for j in range(1,size-abs(i)))
        string = string2 + string + string2[::-1]
        string = string.center(width,'-')
        print(string)