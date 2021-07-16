class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(L):
            ans.append(com.copy())
            for i in range(len(nums)):
                if L<i:
                    com.append(nums[i])
                    dfs(i)
                    com.pop()
        ans=[]
        com=[]
        dfs(-1)
        return ans