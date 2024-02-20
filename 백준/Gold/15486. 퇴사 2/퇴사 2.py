# 어딘가에서 배낀 풀이
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    dp = [-10000000 for _ in range(n+1001)]
    dp[n] = 0

    for i in range(n)[::-1]:
        dp[i] = max(dp[i + arr[i][0]] + arr[i][1], dp[i + 1])

    print(dp[0])

main()