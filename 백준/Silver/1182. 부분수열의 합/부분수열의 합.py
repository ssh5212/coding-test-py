global N, S, arr, answer


def recursive(index, total):
    global N, S, arr, answer

    if index == N:
        if total == S:
            answer += 1
        return

    recursive(index + 1, total + arr[index])
    recursive(index + 1, total)


def main():
    global N, S, arr, answer
    N, S = map(int, input().split())

    arr = list(map(int, input().split()))

    answer = 0

    recursive(0, 0)

    if S == 0:
        print(answer - 1)
    else:
        print(answer)


main()