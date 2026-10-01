class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        r=0
        maxr=nums[0]
        maxsub=0

        while r<len(nums):
            if maxsub+nums[r]<nums[r]:
                maxsub=nums[r]
            else:
                maxsub+=nums[r]
            maxr=max(maxsub,maxr)
            r+=1
        return maxr

        