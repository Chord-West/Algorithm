from itertools import combinations

def solution(nums):
    answer = 0
    primes = [ 0 for i in range(10000)]
    for i in range(2,10000):
        if primes[i]==0:
            for j in range(i*2,10000,i):
                primes[j]=1
    threesum = sorted(([sum(x) for x in combinations(nums,3)]))
    for t in threesum:
        if primes[t]==0:
            answer+=1
    return answer