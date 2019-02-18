import itertools, math

N = int(input())
L = [list(map(int, input().split())) for i in range(N)]

seq = [ i for i in range(N)]
ptr = list(itertools.combinations(seq,2))
res = -1

for p in ptr:
    tmp = math.sqrt((L[p[0]][0] - L[p[1]][0])**2 + (L[p[0]][1] - L[p[1]][1])**2)
    if tmp > res:
        res = tmp
        
print(res)
