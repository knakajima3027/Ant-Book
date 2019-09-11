import heapq 

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
heapq.heapify(A)

time = 0
for i in range(K):
    hq = heapq.heappop(A)
    time += hq[0]
    heapq.heappush(A, [hq[0] + hq[1], hq[1]])

print(time)
