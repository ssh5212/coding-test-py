# 사르르 녹는 치즈.. 맛있겠당..
from collections import deque

def del_cheese():
    global counter
    for x, y in del_cheese_list:
        arr[x][y] = 0

    counter += 1

def bfs():
    q = deque()
    q.append([0, 0])
    v[0][0] = True

    while(len(q) != 0):
        x, y = q.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if v[nx][ny] == True:
                continue

            if arr[nx][ny] == 0:
                q.append([nx, ny])
                v[nx][ny] = True

            if arr[nx][ny] == 1:
                del_cheese_list.append([nx, ny])
                v[nx][ny] = True


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

counter = 0
last_cheese_cnt = 0
del_cheese_list = []

while(True):
    v = [[False] * m for i in range(n)]
    last_cheese_cnt = len(del_cheese_list)
    del_cheese_list = []
    bfs()

    if len(del_cheese_list) == 0:
        break
    del_cheese()

print(counter)
print(last_cheese_cnt)