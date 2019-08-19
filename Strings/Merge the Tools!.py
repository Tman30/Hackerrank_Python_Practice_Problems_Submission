def merge_the_tools(string, k):
    for i in range(int(len(string)/k)):
        print("".join(list(dict.fromkeys(list(string[i*k:(i+1)*k])))))