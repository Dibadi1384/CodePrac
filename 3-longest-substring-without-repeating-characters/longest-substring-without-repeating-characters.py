class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res=1

        if not s:
            return 0

        for i in range(len(s)):
            r=i+1
            length=1
            window={}
            window[s[i]]=i
            while r<len(s) and s[r] not in window :
                window[s[r]]=r
                length+=1
                r+=1
                res=max(res,length)

        return res
                    



        