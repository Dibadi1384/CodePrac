from sortedcontainers import SortedDict
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        res=[]
        mp=SortedDict(list)
        numarray=[]

        for log in logs:
            firstspace=log.find(" ")
            identifier=log[0: firstspace]
            l=log[firstspace+1:len(log)]
            
            if l[0].isdigit():
                numarray.append(log)
            else:
                if l in mp:
                    mp[l].append(identifier)
                    mp[l].sort()
                else:
                    mp[l]=[identifier]

        for log in mp:
            for identifier in mp[log]:
                res.append(identifier+" "+log)
        res+=numarray 

        return res



            

        