# 신맛은 재료의 곱, 쓴맛은 합
# 재료는 하나 이상 사용해야 함
# 신맛과 쓴맛의 차이가 가장 작은 요리 만들기
import sys

global N, arr, v, answer


def recursive(index, sin, sun):
    global N, arr, v, answer

    if index == N:
        if sun == 0: return
        answer = min(answer, abs(sin - sun))
        return

    recursive(index + 1, sin * arr[index][0], sun + arr[index][1])
    recursive(index + 1, sin, sun)


def main():
    global N, arr, v, answer
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    v = [False] * N

    answer = sys.maxsize
    recursive(0, 1, 0)
    print(answer)


main()