N = input()

for x in ('+', '-'):
    for y in ('+', '-'):
        for z in ('+', '-'):
            res = int(N[0])
            
            if x == '+':
                res += int(N[1])
            else:
                res -= int(N[1])
                
            if y == '+':
                res += int(N[2])
            else:
                res -= int(N[2])
                
            if z == '+':
                res += int(N[3])
            else:
                res -= int(N[3])
                
            if res == 7:
                result = N[0] + x + N[1] + y + N[2] + z + N[3] + '=7'
                break
    
print(result)
                
