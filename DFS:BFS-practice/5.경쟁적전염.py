from collections import deque

n, k = map(int, input().split())

graph = []  # total board
data = []  # virus

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
queue = deque(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

target_s, target_x, target_y = map(int, input().split())

while queue:
    virus, s, x, y = queue.popleft()

    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((graph[nx][ny], s+1, nx, ny))
print(graph[target_x-1][target_y-1])
