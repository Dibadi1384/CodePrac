class Solution:
    def minOperations(self, s: str) -> int:
        
        window=deque()
        res=0


        for string in s:
            if window and string==window[-1]:
                window.pop()
                res+=1
                continue
            window.append(string)
            
        return res

