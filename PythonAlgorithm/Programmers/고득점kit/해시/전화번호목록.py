from collections import defaultdict

def solution(phone_book):
    answer=True
    phone_book.sort()
    p = defaultdict(int)
    for phone in phone_book:
        p[phone]=1
    for phone in phone_book:
        tmp=''
        for char in phone:
            tmp+=char
            if tmp in p and tmp !=phone:
                answer=False
    return answer