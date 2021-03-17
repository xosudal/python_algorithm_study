# page 118

n, m = map(int, input().split())

x, y, position = map(int, input().split())

visited = [[False] * m for _ in range(n)]

visited[x][y] = True

Map = list()

for i in range(n):
    Map.append(list(map(int, input().split())))

move = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def turn():
    global position
    position -= 1
    if position == -1:
        position = 3


turn_count = 0
result = 1
while True:
    turn()
    newX = x + move[position][0]
    newY = y + move[position][1]
    if visited[newX][newY] is False and Map[newX][newY] == 0:
        visited[newX][newY] = True
        x = newX
        y = newY
        result += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - move[position][0]
        ny = y - move[position][1]
        if Map[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
        turn_count = 0
print(result)
