# 투포인터 활용 Runtime : 2208 ms


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        num_set = set()

        for i in range(len(nums)):
            num_zero = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp_sum = num_zero + nums[left] + nums[right]
                if tmp_sum < 0:
                    left += 1
                elif tmp_sum > 0:
                    right -= 1
                else:
                    num_set.add((num_zero, nums[left], nums[right]))
                    left += 1
                    right -= 1
        for n in num_set:
            answer.append(list(n))
        return answer