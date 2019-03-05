N, K = map(int, input().split())
L = [int(input()) for _ in range(N)]

flag = False
for i in range(N):
    if L[i] == 0:
        flag = True
        break

if flag:
    print(N)
else:
    s = 0
    t = 0
    count = 1
    tmp = 0
    res = 0
    for _ in range(N * 10):
        count = count * L[t]
        
        if count > K:
            res = max(res, tmp)
            tmp -= 1
            count //= L[s]
            if s != t:
                count //= L[t]
            s += 1
            
        else:
            tmp += 1
            t += 1

        if s  == t + 1:
            t += 1
            
        if t == N:
            res = max(res, tmp)
            break
        
    print(res)

