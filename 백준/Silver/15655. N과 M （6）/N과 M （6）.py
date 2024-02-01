global n, m, sel, arr


def recursive(count, index):
    if count == m:
        for i in sel:
            print(i, end=" ")
        print()
        return

    for i in range(index, n):
        sel[count] = arr[i]
        recursive(count + 1, i + 1)
        sel[count] = 0


def main():
    global n, m, sel, arr
    n, m = map(int, input().split(" "))

    arr = list(map(int, input().split(" ")))
    arr.sort()
    sel = [0] * m
    recursive(0, 0)


main()