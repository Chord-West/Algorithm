def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        tmp=[]
        for i in range(len(a)):
            tmp.append(a[i]+b[i])
        answer.append(tmp)
    return answer