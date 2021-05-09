def solution(s):
    answer = []
    expressions = s[2:-2].split('},{')
    arr = [list(map(int, expression.split(','))) for expression in expressions]
    arr.sort(key=len)
    for a in arr:
        for y in a:
            if y not in answer:
                answer.append(y)

    return answer