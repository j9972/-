from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [-1] * (n+1)
distance[x] = 0

data = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

q = deque([x])

while q:
    now = q.popleft()

    for next in data[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
