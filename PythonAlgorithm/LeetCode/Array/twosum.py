# 브루트포스 : Runtime 4056ms , Memory 14.8 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# in 을 이용한 탐색 : Runtime 644ms , Memory 14.9
# 브루트포스랑 같은 O(n^2)이라도 in 연산쪽이 더 빠르다.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                return [i, nums[i + 1:].index(complement) + (i + 1)]

# 딕셔너리를 이용해 첫번째 수를 뺀 결과 키 조회 : Runtime 52ms , Memory : 15.3MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            num_dict[n] = i
        for i, n in enumerate(nums):
            if target - n in num_dict and i != num_dict[target - n]:
                return [i, num_dict[target - n]]
