# Runtime 44ms,

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(L):
            if L == N:
                # print(arr)
                ans.append(arr.copy())
                return
            else:
                for i in range(N):
                    if visited[i] == 0:
                        visited[i] = 1
                        arr[L] = nums[i]
                        dfs(L + 1)
                        visited[i] = 0

        N = len(nums)
        ans = []
        visited = [0] * N
        arr = [0] * N
        dfs(0)

        return ans

# itertools 사용했을때 Runtime 28 ms
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        arr = list(permutations(nums,len(nums)))
        return arr