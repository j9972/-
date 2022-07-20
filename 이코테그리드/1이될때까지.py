import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int, input().split())
res = 0

while n >= k:
    if n % k != 0:
        n -= 1
        res += 1
    n //= k
    res += 1

while n > 1:
    n -= 1
    res += 1

print(res)
