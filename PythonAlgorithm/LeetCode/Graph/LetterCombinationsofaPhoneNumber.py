class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(L, word):
            if L == len(digits):
                ans.append(word)
            else:
                for i in range(len(letters[L])):
                    if visited[L][i] == 0:
                        visited[L][i] = 1
                        dfs(L + 1, word + letters[L][i])
                        visited[L][i] = 0

        letters = []
        visited = []
        ans = []
        p = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        for digit in digits:
            if digit in p:
                letters.append(p[digit])
                visited.append([0 for _ in range(len(p[digit]))])
        if len(letters) > 0:
            dfs(0, '')
        return ans