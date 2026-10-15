class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        contentmap=defaultdict(list)
        rootres=[]
        res=[]

        for path in paths:
            p=path.split(" ")
            root=p[0]

            for f in range(1,len(p)):
                fl=p[f]

                bracketind=fl.find("(")
                name=fl[0:bracketind]
                content=fl[bracketind:len(fl)-1]
                
                contentmap[content].append(root+"/"+name)
        
        duplicates=False
        print(contentmap)
        for content in contentmap:
            if len(contentmap[content])>1:
                rootres=[]
                duplicates=True
                for path in contentmap[content]:
                    print(path)
                    rootres.append(path)
            if duplicates:
                res.append(rootres)
            duplicates=False
        return res
        