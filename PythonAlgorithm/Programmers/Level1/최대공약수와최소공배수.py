def gcd(a,b):
    while b!=0:
        t = a%b
        a,b = b,t
    return a
def lcm(a,b):
    return a*b//gcd(a,b)
def solution(n, m):
    a,b = max(n,m), min(n,m)
    answer=[gcd(a,b),lcm(a,b)]
    return answer