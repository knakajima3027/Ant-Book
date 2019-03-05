import itertools

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]

for l in L:
    l[0] -= 1
    l[1] -= 1

link = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            link[i][j] = 1
            
for i in range(M):
    link[L[i][0]][L[i][1]] = 1
    link[L[i][1]][L[i][0]] = 1
    
#n桁のm値のbitを生成
def bit(n, m):
    bit_list = list(itertools.product([i for i in range(m)], repeat=n))
    return bit_list

ptr = bit(N, 2)

res = 0
for p in ptr:
    flag = True
    tmp = 0
    for i in range(N):  
        if p[i] == 1:        
            for j in range(N):
                if p[j] == 1 and link[i][j] == 1:
                    for k in range(N):
                        if p[k] == 1 and link[j][k] != 1:
                            flag = False
                    
            tmp += 1
    
    if flag:
        res = max(res, tmp)
            
print(res)
