class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        res=[]
        mp={}
        for d in cpdomains:
            s=d.split(" ")
            rep=int(s[0])
            levels=s[1].split(".")

            domains=[]
            for i, level in enumerate(levels):
                domain=""
                for j in range(i, len(levels)-1):
                    domain+=levels[j]+"."
                domain+=levels[len(levels)-1]
                domains.append(domain)
                
            for domain in domains:
                if domain in mp:
                    mp[domain]+=rep
                else:
                    mp[domain]=rep

        for domain in mp:
            rep=mp[domain]
            string=str(rep)+" "+domain
            res.append(string)
        return res



        