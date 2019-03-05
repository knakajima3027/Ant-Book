N, M = map(int, input().split())
tmp = N
count = 0
for i in range(10**9):
    if tmp > M:
        break
    tmp *= 2
    count += 1
    
print(count)

