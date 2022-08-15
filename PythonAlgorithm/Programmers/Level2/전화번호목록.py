def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x:len(x))
    while phone_book:
        x = phone_book.pop(0)
        for y in phone_book:
            if x==y[:len(x)]:
                return False
    return answer
