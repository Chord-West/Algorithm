import math
def solution(n):
    num = math.sqrt(n)
    if math.sqrt(n) == int(math.sqrt(n)) :
        return pow(num+1, 2)
    return -1