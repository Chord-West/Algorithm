import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline
T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    f = 1
    while (x <= M * N):
        if x % N == y % N:
            print(x)
            f = 0
            break
        x += M
    if f:
        print(-1)