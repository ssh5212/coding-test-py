def dfs(now):
    global ans
    ans += 1
    v[now] = True

    for i in graph[now]:
        if v[i] == False:
            dfs(i)


n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)] # 인접 리스트
v = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
dfs(1)
print(ans - 1)