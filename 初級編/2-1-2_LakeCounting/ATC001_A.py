#pypyじゃないと実行時間で引っかかった

from queue import LifoQueue

H, W = map(int, input().split())
L = [ list(input()) for i in range(H)]
result = "No"
q = LifoQueue()
flag = [[ -1 for i in range(W)] for i in range(H)]

      
for y in range(H):
    for x in range(W):
        if L[y][x] == 's':
            sx, sy = x, y
        if L[y][x] == 'g':
            gx, gy = x, y
            
q.put([sx, sy])
flag[sy][sx] = 1

while q.empty() == False:
    x, y = q.get()
    
    if x == gx and y == gy:
        result = "Yes"
        break
    
    for i, j in ([0,1], [0,-1], [1,0], [-1,0]):
        if 0 <= x + i < W and 0 <= y + j < H and flag[y+j][x+i] == -1 and L[y+j][x+i] != "#":
            q.put([x+i, y+j])
            flag[y+j][x+i] = 1
    
print(result)
