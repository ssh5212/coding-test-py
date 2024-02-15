global N, arr, answer


def recursive(count, benefit):
    global N, arr, answer

    if count > N:
        return

    if count == N:
        answer = max(answer, benefit)
        return

    recursive(count + arr[count][0], benefit + arr[count][1])
    recursive(count + 1, benefit)


def main():
    global N, arr, answer
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    answer = 0

    recursive(0, 0)

    print(answer)


main()