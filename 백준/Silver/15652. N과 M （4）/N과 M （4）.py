global arr, sel, v, n, m

def recursive(count, index):
    if count == m:
        for i in sel:
            print(i, end=" ")
        print()
        return

    for i in range(index, n):
        # if v[i] == True: continue
        # v[i] = True
        sel[count] = arr[i]
        recursive(count + 1, i)
        sel[count] = 0
        # v[i] = False

def main():
    global n, m, arr, sel, v
    n, m = map(int, input().split(" "))
    arr = [i for i in range(1, n + 1)]
    # v = [False] * n
    sel = [0] * m

    recursive(0, 0)

main()