from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

L = [ input() for i in range(R)]
dist = [[ -1 for i in range(C)] for i in range(R)]

q = deque([])
q.append([sy-1, sx-1])
dist[sy-1][sx-1] = 0

while True:
    y, x = q.popleft()
    
    if y == gy-1 and x == gx-1:
        res = dist[y][x]
        break
    
    for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
        if L[y+i][x+j] == '.' and dist[y+i][x+j] == -1:
            q.append([y+i, x+j])
            dist[y+i][x+j] = dist[y][x] + 1
            
print(res)
