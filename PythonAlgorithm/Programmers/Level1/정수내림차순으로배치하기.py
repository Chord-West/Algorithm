def solution(n):
    answer = [int(x) for x in str(n)]
    answer.sort(reverse=True)
    answer=int(''.join(map(str,answer)))
    return answer