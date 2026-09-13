class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        maxlevel=0
        while l<r:
            waterlevel=(min(height[l],height[r]))*(r-l)
            maxlevel=max(maxlevel,waterlevel)

            if height[l]<=height[r]:
                l+=1
            else:
                r-=1

        return maxlevel


        