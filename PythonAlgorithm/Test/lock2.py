import sys
import copy
from collections import deque

def main():
    sys.stdin = open("sample_input.txt","rt")
    input = sys.stdin.readline
    T = int(input())
    for t in range(1, T + 1):
        ans = 9999999999
        n, k = map(int, input().split())
        col_loca = [[] for _ in range(n)]
        row_loca = [[] for _ in range(k)]
        lock = [[0] * n for _ in range(k)]
        for i in range(k):
            for j, v in enumerate(input().rstrip('\n')):
                if v == '1':
                    col_loca[j].append(i)
                    row_loca[i].append(j)
                    lock[i][j] = 1
        mr = max(len(l) for l in row_loca)
        q = deque([])
        for i in range(len(row_loca)):
            if len(row_loca[i]) == mr:
                q.append(i)
        print(q)
        while q:
            y = q.popleft() # 1이 제일 많이 있는 행
        # y= q.popleft()
        # y = q.popleft()
            tmp_s=0
            for col in col_loca:
                tmp_m=k
                for c in col:
                    if y > c:
                        tmp=min(y-c,(k-y)+c)
                    else:
                        tmp=min(c-y,(k-c)+y)
                    if tmp_m>tmp:
                        tmp_m=tmp
                tmp_s+=tmp_m
            if ans>tmp_s:
                ans=tmp_s
        print('#{} {}'.format(T, ans))


main()