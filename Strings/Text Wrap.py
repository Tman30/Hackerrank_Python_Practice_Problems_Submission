def wrap(string, max_width):
    return "\n".join(string[max_width*i:max_width*i +max_width] for i in range(len(string)))