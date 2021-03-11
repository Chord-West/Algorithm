def solution(arr1, arr2):
    answer = []
    for x_row in arr1:
        li=[]
        for y_col in zip(*arr2):
            sum=0
            for a,b in zip(x_row,y_col):
                sum+=a*b
            li.append(sum)
        answer.append(li)
    return answer