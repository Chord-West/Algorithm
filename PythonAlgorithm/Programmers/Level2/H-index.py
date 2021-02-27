def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for x in citations:
        if x > answer:
            answer+=1
    return answer