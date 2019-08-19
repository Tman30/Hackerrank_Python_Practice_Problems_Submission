def print_formatted(num):
    width = len("{0:b}".format(num))
    for i in range(1,num+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width))