N, Y = map(int, input().split())
rx, ry, rz = -1, -1, -1

for x in range(N+1):
    for y in range(N+1-x):
            if Y - 10000*x - 5000*y - 1000*(N-x-y) == 0:
                rx, ry, rz = x, y, (N-x-y)
                break
    
print(rx, ry, rz)
