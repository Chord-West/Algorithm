def solution(arr, divisor):
    answer = sorted([x for x in arr if x%divisor==0])
    return answer if len(answer)!=0 else [-1]