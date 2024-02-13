import sys

global N, M, arr, answer, v, answerSong


def recursive(count):
    global N, M, arr, answer, v, answerSong

    if count == N:
        counter = 0
        canPlay = [False] * M
        for i in range(N):  # 기타 개수
            if v[i] == False:  # 선택하지 않은 기타라면
                continue

            counter += 1
            for j in range(M):  # 음악 개수
                if arr[i][j] == 'Y':
                    canPlay[j] = True

        nowSong = 0
        for i in range(M):
            if canPlay[i] == True:
                nowSong += 1

        if answerSong < nowSong:
            answerSong = nowSong
            answer = counter
        elif answerSong == nowSong:
            answer = min(answer, counter)

        return

    v[count] = True
    recursive(count + 1)
    v[count] = False
    recursive(count + 1)


def main():
    global N, M, arr, answer, answerSong, v

    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        _, playlist = map(str, input().split(" "))
        arr.append(list(playlist))

    v = [False] * N
    answer = 0
    answerSong = 0

    recursive(0)

    if answerSong == 0:
        print(-1)
    else:
        print(answer)


main()