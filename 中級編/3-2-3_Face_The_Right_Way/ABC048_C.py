N, x = map(int, input().split())
L = list(map(int, input().split()))
res = 0
for i in range(N-1):
    if L[i] + L[i+1] > x:
        if L[i] <= x:
            res +=  L[i+1] - (x - L[i])
            L[i+1] =  x - L[i]
        else:
            res += L[i+1] + L[i] - x
            L[i] = x
            L[i+1] = 0
            
print(res)

