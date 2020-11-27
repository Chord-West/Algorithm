
def dfs(numbers,count,sum,target):
    if count==5:
        return 0
        if sum == target:
           return sum
    dfs(numbers,count+1,sum+numbers[count],target)
    dfs(numbers,count+1,sum-numbers[count],target)
    return 0

def solution(numbers, target):
    answer=0
    answer=answer+dfs(numbers,0,sum,target)
    return answer

numbers = [1,1,1,1,1]
target=3
print(solution(numbers,target))