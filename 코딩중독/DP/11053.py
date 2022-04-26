import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if a[i] > a[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1

    print(max(dp))
