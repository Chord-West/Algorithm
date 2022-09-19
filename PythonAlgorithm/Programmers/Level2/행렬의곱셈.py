def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        tmp=[]
        for a2 in zip(*arr2):
            tmp.append(sum(x*y for x,y in zip(a1,a2)))
        answer.append(tmp)
    return answer