

def solution(numbers, target):
    answer=0
    n = len(numbers)

    def dfs(cnt,sum):
        if cnt==n: 
            if sum == target:
                nonlocal answer
                answer+=1
        else:
            dfs(cnt+1,sum+numbers[cnt])
            dfs(cnt+1,sum-numbers[cnt])
    dfs(0,0)

    return answer


numbers = [1,1,1,1,1]
target=3
print(solution(numbers,target))