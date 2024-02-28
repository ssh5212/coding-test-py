dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def move_cloud(dd, ss):
    global cloud_arr, cloud_list

    for i in range(len(cloud_list)):
        nx = (dx[dd] * ss + cloud_list[i][0] + n) % n
        ny = (dy[dd] * ss + cloud_list[i][1] + n) % n

        cloud_list[i][0] = nx
        cloud_list[i][1] = ny

    change_cloud_arr()


def append_water():
    global arr

    for x, y in cloud_list:
        arr[x][y] += 1


dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, 1, -1]


# def delete_cloud():
def water_copy():
    global arr
    arr_copy = [[0] * n for i in range(n)]  # 정보는 이걸로 받고 arr에 변경 정보 저장

    for i in range(n):
        for j in range(n):
            arr_copy[i][j] = arr[i][j]

    for i in range(n):
        for j in range(n):
            if cloud_arr[i][j] == True:
                for d in range(len(dx2)):
                    nx = dx2[d] + i
                    ny = dy2[d] + j

                    if nx >= 0 and nx < n and ny >= 0 and ny < n and arr_copy[nx][ny] >= 1:
                        arr[i][j] += 1


def create_cloud():
    global arr, cloud_list

    cloud_list = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and cloud_arr[i][j] == False:
                cloud_list.append([i, j])
                arr[i][j] -= 2

    change_cloud_arr()


def change_cloud_arr():
    global cloud_arr, cloud_list

    cloud_arr = [[False] * n for i in range(n)]

    for i in range(len(cloud_list)):
        cloud_arr[cloud_list[i][0]][cloud_list[i][1]] = True


def change_cloud_list():
    global cloud_arr, cloud_list

    cloud_list = []

    for i in range(n):
        for j in range(n):
            if cloud_arr[i][j] == True:
                cloud_list.append([i, j])


# 첫 번째 줄
n, m = map(int, input().split(" "))  # n : 행렬 크기 / m : 비바라기 시전 횟수

# n개의 줄
arr = []  # 지도
for i in range(n):
    arr.append(list(map(int, input().split(" "))))

move_list = []  # 움직여야 할 방향과 횟수 정보

for i in range(m):
    move_list.append(list(map(int, input().split(" "))))

cloud_arr = [[False] * n for i in range(n)]  # 구름 정보 지도에 저장
cloud_list = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]  # 구름 정보 리스트에 저장

change_cloud_arr()  # 구름 리스트 -> 지도로 변환
change_cloud_list()  # 구름 지도 -> 리스트로 변환

# 기능 구현
for d, s in move_list:
    move_cloud(d, s)
    append_water()
    # delete_cloud()
    water_copy()
    create_cloud()

answer = 0
for i in range(n):
    for j in range(n):
        answer += arr[i][j]
print(answer)