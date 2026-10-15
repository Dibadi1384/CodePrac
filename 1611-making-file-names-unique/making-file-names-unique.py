class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        hp={}
        res=[]

        for name in names:
            if name not in hp:
                hp[name]=1
                res.append(name)
                continue

            counter=hp[name]
            filename=f"{name}({counter})"
            while filename in hp:
                counter+=1
                filename=f"{name}({counter})"
                
            hp[filename]=1
            hp[name]=counter+1
            res.append(filename)
        return res

        