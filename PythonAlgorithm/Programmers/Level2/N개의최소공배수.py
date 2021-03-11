from math import gcd
def solution(arr):
    while len(arr)!=1:
        x,y = arr.pop(0),arr.pop(0)
        arr.append(x*y//gcd(x,y))
    return arr[0]