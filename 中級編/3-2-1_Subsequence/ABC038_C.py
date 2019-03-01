N = int(input()) 
L = list(map(int, input().split()))

tmp = [0 for _ in range(N)]

for i in range(N-1):
    if L[i+1] > L[i]: 
        tmp[i+1] = tmp[i] + 1

res = N
for i in range(N):
    res += tmp[i]
    
print(res)
