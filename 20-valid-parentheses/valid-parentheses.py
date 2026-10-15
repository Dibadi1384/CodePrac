class Solution:
    def isValid(self, s: str) -> bool:
        opens={'(': ')', '{': '}', '[':']'}
        openingb=deque()

        if len(s)<2:
            return False

        for b in s:
            if b in opens:
                openingb.append(b)
            else:
                if not openingb:
                    return False
                openbracket=openingb.pop()
                if b!=opens[openbracket]:
                    return False

        
        if openingb:
            return False
        return True

        