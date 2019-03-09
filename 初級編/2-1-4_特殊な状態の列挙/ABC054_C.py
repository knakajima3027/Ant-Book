N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]

import itertools
ptr = list(itertools.permutations(V, N))

res = 0
for p in ptr:       
    if p[0] == 1:
        now = 1
        flag = [0 for _ in range(N)]
        flag[0] = 1
        for i in range(N-1):
            for j in range(M):
                if A[j][0] == now and A[j][1] == p[i+1]:
                    flag[A[j][1] - 1] += 1
                    now = p[i+1]
                if A[j][1] == now and A[j][0] == p[i+1]:
                    flag[A[j][0] - 1] += 1
                    now = p[i+1]
                    
        tmp = 1         
        for i in range(N):
            if flag[i] != 1:
                tmp = 0
                break
                
        res += tmp
 
print(res)
