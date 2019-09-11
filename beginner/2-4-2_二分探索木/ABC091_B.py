N = int(input())
L = [ input() for _ in range(N)]
M = int(input())
K = [ input() for _ in range(M)]

dic = {}

for l in L:
    if l in dic:
        dic[l] += 1
    else:
        dic[l] = 1
        
for k in K:
    if k in dic:
        dic[k] -= 1
    else:
        dic[k] = -1

res = 0
for i in dic:
    res = max(res, dic[i])
    
print(res)
