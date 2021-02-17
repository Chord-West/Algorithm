def solution(phone_number):
    L = len(phone_number)-4
    answer = '*'*L+phone_number[L:]
    return answer