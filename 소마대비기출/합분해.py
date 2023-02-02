#골드5 - 2225 - 다시
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[0] * (n+1) for _ in range(k+1)]
d[0][0] = 1

for i in range(1, k+1):
    for j in range(n+1):
        d[i][j] = d[i-1][j] + d[i][j-1]
print(d[k][n] % 1000000000)
