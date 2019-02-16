```
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp
```

N, W = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(W+1)] for i in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if L[N-i-1][1] > j:
            dp[N-i-1][j] = dp[N-i][j]
        else:
            dp[N-i-1][j] = max(dp[N-i][j], dp[N-i][j-L[N-i-1][1]] + L[N-i-1][0])

res = -1
for i in range(W+1):
    for j in range(N+1):
        res = max(res, dp[j][i])

print(res)
