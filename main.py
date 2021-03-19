# this is main file

n = int(input())

photo = []

photo_set = set()

for i in range(n):
    input_list = list(map(int, input().split()))
    photo_set.add(input_list[1])
    photo.append((input_list[0], input_list[1]))

photo.sort(key=lambda photo_list: photo_list[0])

check_id = [0] * 50000

while True:
    start_index = 0
    end_index = 0
    ps = set()
    while len(ps) != len(photo_set):
        ps.add(photo[end_index][1])
        #check_id[photo[end_index][1]] += 1
        print("check :", photo[end_index][1])
        print(ps)
        end_index += 1

    if len(ps) == len(photo_set):
        break

#print(check_id)

print(photo)

print(photo_set)
