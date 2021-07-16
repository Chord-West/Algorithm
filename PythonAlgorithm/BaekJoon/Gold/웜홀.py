import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N,M,W = map(int,input().split())
    node =[[] for _ in range(N+1)]

    for _ in range(M): # 도로
        S,E,T = map(int,input().split())
    for _ in range(W): # 웜홀
        S,E,T = map(int,input().split())
