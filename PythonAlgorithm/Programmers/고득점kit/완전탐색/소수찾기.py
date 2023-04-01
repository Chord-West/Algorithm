from itertools import permutations


def solution(numbers):
    answer = 0
    arr = set()
    prime = [0] * 10000000
    prime[0], prime[1] = 1, 1
    for i in range(2, 10000000):
        if prime[i] == 0:
            for j in range(i * 2, 10000000, i):
                prime[j] = 1

    for i in range(1, len(numbers) + 1):
        for x in list(permutations(map(int, numbers), i)):
            arr.add(int(''.join(map(str, x))))

    for a in arr:
        if prime[a] == 0:
            answer += 1
    return answer


