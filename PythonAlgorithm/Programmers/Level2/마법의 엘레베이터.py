def solution(storey):
    answer = 0
    arr = list(map(int,str(storey)))[::-1]
    arr.append(0)
    for i in range(len(arr)):
        if arr[i] > 5:
            answer = answer + 10-arr[i]
            arr[i+1] +=1
        elif arr[i] < 5:
            answer +=arr[i]
        else:
            if arr[i+1]>4:
                answer = answer + 10-arr[i]
                arr[i+1] +=1
            else:
                answer +=arr[i]
    return answer