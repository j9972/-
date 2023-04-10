import sys
input = sys.stdin.readline

n = int(input())

d = []
for i in range(n):
    d.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = d[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = d[i-1][j]
        
        d[i][j] += max(left_up,up)

res = 0
for i in range(n):  
    res = max(res, d[n-1][i])
print(res)

