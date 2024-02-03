global n, s, arr, v, answer


def recursive(count):
    global n, s, arr, v, answer

    if count == n:
        nowAns = 0
        count = 0
        for i in range(n):
            if v[i] == True:
                nowAns += arr[i]
                count += 1
        if nowAns == s and count != 0:
            answer += 1

        return

    v[count] = True
    recursive(count + 1)
    v[count] = False
    recursive(count + 1)


def main():
    global n, s, arr, v, answer

    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [False] * n
    answer = 0

    recursive(0)
    print(answer)


main()