

nums = [1,4,3,2]

nums.sort()
print(nums)
sum=0
for i in range(0,len(nums),2):
    sum+=min(nums[i],nums[i+1])

print(sum)
