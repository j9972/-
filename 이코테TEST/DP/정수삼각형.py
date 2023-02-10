import sys
from turtle import left
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]

        if i == j:
            up = 0
        else:
            up = d[i-1][j]

        d[i][j] += max(left_up, up)

print(max(d[n-1]))
