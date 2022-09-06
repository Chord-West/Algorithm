import sys

sys.stdin = open("input.txt","rt")
N,H = map(int,input().split())

trees = list(map(int,input().split()))
trees.sort()
lt,rt = 1, trees[-1]

while lt<=rt:
    mid = (lt+rt)//2
    sum_h = sum( t-mid for t in trees if t >= mid)
    if sum_h >= H:
        lt = mid + 1
    else:
        rt = mid - 1

print(rt)




