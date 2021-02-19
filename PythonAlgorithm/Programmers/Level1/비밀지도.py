def solution(n, arr1, arr2):
    answer = []
    for x,y in zip(arr1,arr2):
        tmp=''
        for _ in range(n):
            if x%2==1 or y%2==1:
                tmp+='#'
            else:
                tmp+=' '
            x,y = x//2, y//2
        answer.append(tmp[::-1])
    return answer