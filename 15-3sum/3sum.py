class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        d=defaultdict(list)

        for i,num in enumerate(nums):
            if num in nums:
                d[num].append(i)
            else:
                d[num]=[i]

        res=[]


        for i in range(0, len(nums)-1):
            if i>0 and nums[i-1]==nums[i]:
                continue
            prevj=None
            for j in range(i+1, len(nums)):
                if nums[j]==prevj:
                    continue
                val=0-nums[i]-nums[j]

                if val in d:
                    for k in d[val]:
                        if k<=j:
                            continue
                        else:
                            break
                    if k<=j:
                        continue
                    else:
                        res.append([nums[i], nums[j], nums[k]]) 
                prevj=nums[j]   
        return res
                    

