# this is main file
from collections import deque
import sys

n = int(input())

photo = []
photo_set = set()

for i in range(n):
    dist, photo_id = list(map(int, input().split()))
    photo_set.add(photo_id)
    photo.append([dist, photo_id])

max_len = len(photo_set)

photo.sort(key=lambda photo_list: photo_list[0])

result = sys.maxsize

q = deque()
dq = deque()
index = 0
start_dist = 0
end_dist = 0
while photo:
    while len(set(q)) < max_len and len(photo) > 0:
        dist, photo_id = photo.pop()
        q.append(photo_id)
        dq.append(dist)

    while True:
        if q[index] == q[index + 1]:
            q.popleft()
            dq.popleft()
        else:
            break

    end_dist = dq[0]
    start_dist = dq[len(q)-1]

    if len(set(q)) == max_len:
        #print(q)
        #print("start", start_dist, "end", end_dist)
        result = min(result, end_dist - start_dist)

    q.popleft()

print(result)
