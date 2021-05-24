def solution(height):
    answer = 0
    stan = sorted(set(height), reverse=True)
    for s in stan:
        x = height.index(s)
        for i, h in enumerate(height):
            if h == s:
                answer += i - x + 1
                x = i

    return answer

input =  [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution(input))