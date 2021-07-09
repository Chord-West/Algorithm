import sys

sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
INF = sys.maxsize
N,S = map(int,input().split())
arr = list(map(int,input().split()))
ans = INF
left = 0
right = 1
Sum_arr = [0] * (N + 1)
for i in range(1, N + 1):
    Sum_arr[i] = Sum_arr[i - 1] + arr[i - 1]
while left < N:
    if Sum_arr[right]-Sum_arr[left]>=S:
        ans = min(right-left,ans)
        left+=1
    else:
        if right<N:
            right+=1
        else:
            left+=1
print(0 if ans==INF else ans)