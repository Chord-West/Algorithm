import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

N = int(input())
lines =  [list(map(int,input().split())) for _ in range(N)]
max_line = lines[0]
min_line = lines[0]


for i in range(1,N):
    max_line = [max(max_line[0],max_line[1])+lines[i][0],max(max_line[0],max_line[1],max_line[2])+lines[i][1],
                max(max_line[1],max_line[2])+lines[i][2]]
    min_line = [min(min_line[0], min_line[1]) + lines[i][0], min(min_line[0], min_line[1], min_line[2]) + lines[i][1],
                min(min_line[1], min_line[2]) + lines[i][2]]

print(max(max_line),min(min_line))