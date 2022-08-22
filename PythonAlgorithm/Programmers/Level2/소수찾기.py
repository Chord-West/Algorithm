from itertools import permutations
def solution(numbers):
    prnum = set()
    size = 1000000
    prime = [0] * size
    prime[0], prime[1] = 1, 1
    for i in range(2, size):
        if prime[i] != 1:
            for j in range(i * 2, size, i):
                prime[j] = 1

    for i in range(1, len(numbers) + 1):
        for x in permutations(numbers, i):
            n = int(''.join(x))
            if prime[n] == 0:
                prnum.add(n)

    return len(prnum)