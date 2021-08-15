from itertools import permutations

def solution(numbers):
    answer = 0
    isPrime= [0]*pow(10,len(numbers))
    isPrime[0],isPrime[1]=1,1
    for i in range(2,len(isPrime)):
        if isPrime[i]==0:
            for j in range(i+i,len(isPrime),i):
                isPrime[j]=1
    tmp=[]
    for i in range(len(numbers)):
        tmp+=list(map(int, map("".join, permutations(list(numbers), i + 1))))
    tmp=set(tmp)
    for t in tmp:
        if isPrime[t]==0:
            answer+=1
    return answer