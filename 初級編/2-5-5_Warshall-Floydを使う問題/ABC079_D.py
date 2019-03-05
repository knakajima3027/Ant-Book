def warshall_floyd(d, V): #d[i][j]は2頂点間i, j間の移動コストを格納, Vは頂点数
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
                
    return d
                
H, W = map(int, input().split())                
L = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(H)]

cost = warshall_floyd(L, 10)

res = 0
for i in range(H):
    for j in range(W):
        if a[i][j] != -1:
            res += cost[a[i][j]][1]
        
print(res)

