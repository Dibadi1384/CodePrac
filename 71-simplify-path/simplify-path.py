class Solution:
    def simplifyPath(self, path: str) -> str:
        p=path.split("/")
        print(p)
        sp=deque()
        res=""
        for l in p:

            if l=="..":
                if sp:
                    sp.pop()
                else:
                    sp.append("/")

            elif l=="." or l=="/" or l=="":
                continue
            else:
                
                if sp and sp[-1]=="/":
                    sp.append(l)
                else:
                    sp.append("/"+l)
        if not sp:
            return "/"
        while sp:
            level=sp.popleft()
            res+=level
        return res

