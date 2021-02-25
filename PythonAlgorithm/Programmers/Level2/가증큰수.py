def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    numbers = sorted(numbers, key = lambda x:x*3, reverse=True)
    answer=str(int(''.join(numbers)))
    return answer