class Solution:
    def compress(self, chars: list[str]) -> int:
        s=[]
        l,r=0,0
        rep=0

        for char in chars:
            if s and char==s[-1]:
                rep+=1 
            else:
            
                if rep>1:
                    s.extend(str(rep))
                s.append(char)
                rep=1
                
        if rep>1:
            s.extend(str(rep))
        print(s)
        chars[:]=s
        return len(s)

        