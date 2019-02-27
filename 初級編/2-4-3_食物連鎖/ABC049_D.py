class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    
N, K, L = map(int, input().split())
    
p = [list(map(int, input().split())) for _ in range(K)]

r = [list(map(int, input().split())) for _ in range(L)]

res = [1 for _ in range(N)]
    
load = UnionFind(N)
train = UnionFind(N)

for i in range(K):
    load.unite(p[i][0]-1, p[i][1]-1)
    
for i in range(L):
    train.unite(r[i][0]-1, r[i][1]-1)
    
    
dic= {}
for i in range(N):
    tmp = (load.find(i), train.find(i))
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

        
for i in range(N):
    tmp = (load.find(i), train.find(i))
    res[i] = dic[tmp]
    
result = ''
for i in range(N):
    result += str(res[i]) + ' '
    
print(result)

