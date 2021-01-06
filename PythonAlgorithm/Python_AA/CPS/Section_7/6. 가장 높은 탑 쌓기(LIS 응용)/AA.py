#import sys
#sys.stdin = open("input.txt","rt")

# 넓이, 높이, 무게
n = int(input())
brick = [list(map(int,input().split())) for _ in range(n)]
# 밑면 넓이랑 무게만 신경쓰기
brick.sort(reverse=True)
dp=[0]*(n)
dp[0]=brick[0][1] # 높이
res=0
# 높이로 dp 설정
for i in range(1,n):
    max=0
    for j in range(i-1,-1,-1):
        if brick[j][2]>brick[i][2] and dp[j]>max:
            max=dp[j]
    dp[i] = max +brick[i][1]
    if res<dp[i]:
        res=dp[i]

print(res)