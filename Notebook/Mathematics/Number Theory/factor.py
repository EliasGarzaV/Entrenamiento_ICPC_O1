import math
def factor(n):
    pos = [2, 3]
    pos.extend([6 * k + i for k in range(1, math.ceil(n/12) + 1) for i in [-1, 1]])
    pos.append(n)
    primes = []
    exponents = []
    iter = 0
    while(n > 1):
        if(n % pos[iter] == 0):
            primes.append(pos[iter])
            ex = 0
            while(n % pos[iter] == 0):
                n = n / pos[iter]
                ex += 1
            exponents.append(ex)
        iter += 1
    return [primes, exponents]

fact=factor(int(input()))
print(fact[0])
print(fact[1])