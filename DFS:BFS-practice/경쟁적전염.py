from collections import deque
n, k = map(int, input().split())

graph = []  # 전체 보드 정보
data = []  # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:  # 0이 아니라는것은 바이러스가 있다는것
            data.append((graph[i][j], 0, i, j))  # 바이러스 종류 , 시간 ,위치x, 위치y

data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])
