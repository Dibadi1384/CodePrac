class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        #1 2 3 4 100 200 201 202 203 204 205
        maxlen=0
        r=1
       
        if not nums:
            return 0
        if len(nums)<2:
            return 1

        while r<len(nums):
            seq=1
            while r<len(nums) and (nums[r]==(nums[r-1]+1) or nums[r]==nums[r-1]) :
                if nums[r]==nums[r-1]:
                    r+=1
                    continue
                else:
                    seq+=1
                    r+=1
            maxlen=max(maxlen, seq)
            r+=1
        return maxlen

        