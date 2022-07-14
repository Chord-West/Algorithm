def solution(nums):
    set_nums = set(nums)
    answer = len(nums)/2
    if len(set_nums)>=answer:
        return answer
    else:
        return len(set_nums)