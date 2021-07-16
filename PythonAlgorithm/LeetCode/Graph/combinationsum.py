
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(L,S):
            if S==target:
                ans.append(com.copy())
            elif S>target:
                return
            else:
                for i in range(len(candidates)):
                    if candidates[L]<=candidates[i]:
                        com.append(candidates[i])
                        dfs(i,S+candidates[i])
                        com.pop()
        candidates.sort()
        ans=[]
        com=[]
        dfs(0,0)
        return ans