class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1.find(".")>0:
            v1=version1.split(".")
        else:
            v1=[version1]
     
        if version2.find(".")>0:
            v2=version2.split(".")
        else:
            v2=[version2]
        n=abs(len(v1)-len(v2))
        if len(v1)>len(v2):
            v2.extend([0] * n ) 

        elif len(v1)<len(v2):
            v1.extend([0] * n) 
        


        for i in range(len(v1)):
            int1=int(v1[i])
            int2=int(v2[i])
            if int1>int2:
                return 1
            elif int1<int2:
                return -1
            else:
                continue
        return 0
