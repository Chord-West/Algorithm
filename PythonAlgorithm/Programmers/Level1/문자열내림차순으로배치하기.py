def solution(s):
    return ''.join(map(str,sorted(s,reverse=True)))