N = int(input())
L = list(map(int, input().split()))

dp = [[0 for _ in range(sum(L)+1)] for _ in range(N+1)]

i = N
dp[N][0] = 1
for _ in range(N):
    for j in range(sum(L)+1):
        if dp[i][j] == 1:
            dp[i-1][j] = 1
            dp[i-1][j+L[i-1]] = 1
    i -= 1
        
    
print(sum(dp[0]))
