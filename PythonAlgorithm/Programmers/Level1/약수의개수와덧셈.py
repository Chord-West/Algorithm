import math
def solution(left, right):
    return sum(-x if pow(int(math.sqrt(x)),2)==x else x for x in range(left,right+1))