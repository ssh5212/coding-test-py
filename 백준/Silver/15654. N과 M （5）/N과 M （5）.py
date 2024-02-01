global n, m, arr, sel, v

def recursive(count):
    if count == m:
        for i in sel:
            print(i, end=" ")
        print()
        return

    for i in range(n):
        if v[i] == True: continue
        v[i] = True
        sel[count] = arr[i]
        recursive(count + 1)
        sel[count] = 0
        v[i] = False

def main():
    global n, m, arr, sel, v
    # 숫자 개수, 선택할 개수
    n, m = map(int, input().split(" "))

    arr = list(map(int, input().split(" ")))
    arr.sort()
    v = [False] * n
    sel = [0] * m

    recursive(0)

main()