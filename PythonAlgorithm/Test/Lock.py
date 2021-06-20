import sys
from collections import deque
import time

def main():
    sys.stdin = open("sample_input.txt","rt")
    input = sys.stdin.readline
    T = int(input())
    dx=[0,0]
    dy=[1,-1]
    for t in range(1, T + 1):
        ans=9999999999
        n, k = map(int, input().split())
        q = deque([])
        lock = [[0] * n for _ in range(k)]
        for i in range(k):
            for j, v in enumerate(input().rstrip('\n')):
                print(v)
                if v == '1':
                    q.append([i, j])
                    lock[i][j] = 1

        while q:
            y,x = q.popleft()
            tmp=0
            for o in lock[y]:
                tmp+=o
                if o==0:
                    break
            else:
                ans=tmp-n
                break
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=ny<k and lock[ny][nx]==0:
                    lock[ny][nx]=lock[y][x]+1
                    q.append([ny,nx])
                elif ny==-1:
                    ny=k-1
                    if lock[ny][nx]==0:
                        lock[ny][nx] = lock[y][x] + 1
                        q.append([ny, nx])
                elif ny==k:
                    ny=0
                    if lock[ny][nx] == 0:
                        lock[ny][nx] = lock[y][x] + 1
                        q.append([ny, nx])

        print('#{} {}'.format(T,ans))

main()