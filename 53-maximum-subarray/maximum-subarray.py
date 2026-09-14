class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            # Either continue the previous subarray,
            # or start a new subarray at nums[i]
            curr = max(nums[i], curr + nums[i])

            # Keep the best sum we've seen overall
            best = max(best, curr)

        return best