L = [list(input()) for _ in range(10)]

land = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if L[i][j] == 'o':
            land[i][j] = 1

res = 'NO'
for i in range(10):
    for j in range(10):
        n_flag = False
        flag = [[False for _ in range(10)] for _ in range(10)]
        island = [[0 for _ in range(10)] for _ in range(10)]
        if True:
            tmp = L[i][j]
            L[i][j] = 'o'
            land[i][j] = 1
            island[i][j] = 1
            stack = [[i, j]]
            flag[i][j] = True
            while True:
                x, y = stack.pop()
                for nx, ny in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                    if 0<= x + nx < 10 and 0 <= y + ny < 10:
                        if flag[x+nx][y+ny] == False and L[x+nx][y+ny] == 'o':
                            flag[x+nx][y+ny] = True
                            island[x+nx][y+ny] = 1
                            stack.append([x+nx, y+ny])
                        
                if stack == []:
                    break
                    
            for a in range(10):
                for b in range(10):
                    if land[a][b] != island[a][b]:
                        n_flag = True
                        break
                        
            if tmp == 'x':
                L[i][j] = 'x'
                land[i][j] = 0
                        
            if n_flag == False:
                res = 'YES'
                no = False
                break
   
print(res)
                    
