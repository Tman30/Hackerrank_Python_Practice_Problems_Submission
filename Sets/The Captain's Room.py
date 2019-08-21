K = int(input())
room_list = list(map(int, input().split()))
room_list_copy = room_list[:]
rooms = set(room_list_copy)
for i in rooms:
    room_list_copy.remove(i)
    if not i in room_list_copy:
        print(i)
        break