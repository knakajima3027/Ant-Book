N, A, B = map(int, input().split())

alice = A 
bolice = B
while True:
    if alice + 1 != N + 1 and alice + 1 != bolice:
        alice += 1
    else:
        res = 'Borys'
        break

    if bolice - 1 != 0 and  bolice - 1 != alice:
        bolice -= 1
    else:
        res = 'Alice'
        break

print(res)


