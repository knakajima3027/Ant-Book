from collections import deque

result = []

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
        
    L = [list(map(int, input().split())) for i in range(h)]
    flag = [[-1 for _ in range(w)] for _ in range(h)]
    res = 0
    q = deque()
    
    for y in range(h):
        for x in range(w):
            if L[y][x] == 1 and flag[y][x] == -1:
                q.append([y, x])
                flag[y][x] = 0
                res += 1
                while q:
                    ny, nx = q.pop()
                    for i, j in [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1, -1), (-1, 1), (-1, -1)]:
                        if 0 <= ny + i < h and 0 <= nx + j < w:
                            if L[ny + i][nx + j] == 1 and flag[ny + i][nx + j] == -1:
                                q.append([ny + i, nx + j])
                                flag[ny + i][nx + j] = 0
                            
    result.append(res)
                            
        
for res in result:
    print(res)
    
    
