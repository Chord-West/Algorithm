
def solution(numbers):
    return str(int(''.join(sorted(map(str,numbers),key=lambda x:x*4,reverse=True))))