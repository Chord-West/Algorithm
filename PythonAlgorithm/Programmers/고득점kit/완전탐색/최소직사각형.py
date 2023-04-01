def solution(sizes):
    p = sorted( [ sorted(size, reverse=True) for size in sizes],reverse=True)
    return p[0][0] * max(p, key = lambda x:x[1])[1]