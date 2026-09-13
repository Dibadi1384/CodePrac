class Solution:
    def isValid(self, s: str) -> bool:
        starts={'(':')', '{':'}', '[':']'}
        start=deque()

        for paran in s:
            if paran in starts:
                start.append(paran)
            else:
                if start and starts[start.pop()]==paran:
                    continue
                else:
                    return False
        
        if not start:
            return True
        return False
        
