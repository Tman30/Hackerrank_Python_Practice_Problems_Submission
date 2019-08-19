def getkey(item):
    return(item[1])
final = []
if __name__ == '__main__':
    sec_minimum = 0
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        temp = [name,score]
        students.append(temp)
    #print(students)
    students.sort(key = getkey)
    #print(students)
    minimum = students[0][1]
    #print(minimum)
    for i in students:
        if i[1] > minimum:
            if not sec_minimum:
                sec_minimum = i[1]
                final.append(i[0])
            elif sec_minimum == i[1]:
                final.append(i[0])
    final.sort()
    for i in final:
        print(i)