import sys
sys.stdin = open("input.txt","rt")
r = sys.stdin.readline

n = int(r())
arr = list(map(int,r().split()))
arr.sort()
answer=0
for i in range(n):
    for j in range(n-i):
        answer+=arr[j]
print(answer)