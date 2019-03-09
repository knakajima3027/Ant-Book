N = int(input())
K = int(input())
A = [int(input()) for _ in range(N)]

import itertools

ptr = list(itertools.permutations(A, K))

res = []
for p in ptr:       
    tmp = ''
    for i in range(len(p)):
        tmp += str(p[i])            
    res.append(tmp)
 
res = len(set(res))
print(res)
