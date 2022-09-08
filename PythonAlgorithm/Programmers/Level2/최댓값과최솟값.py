def solution(s):
    L = sorted(map(int,s.split()))
    return '{} {}'.format(L[0],L[-1])