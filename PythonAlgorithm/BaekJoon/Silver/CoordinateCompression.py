import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline

n = r()
tmp = list(map(int,r().split()))
arr = sorted(set(tmp))
p = {arr[i]:i for i in range(len(arr))}
answer= [p[i] for i in tmp]
print(*answer)