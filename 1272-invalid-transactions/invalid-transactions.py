class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        mp=defaultdict(deque)
        resmap={}
        res=[]
        counts = Counter(transactions)

        for transaction in transactions:
            t=transaction.split(",")
            name,time,amount,city=t[0],int(t[1]),int(t[2]),t[3]

            inv=False
            if name in mp:
                for prevtransaction in mp[name]:
                    prevtime,prevamount,prevcity=prevtransaction[0],prevtransaction[1],prevtransaction[2]
                    if abs(time - prevtime) <= 60 and prevcity != city:
                        pt=name+","+ str(prevtime)+","+ str(prevamount)+","+ prevcity
                        if pt not in resmap:
                            resmap[pt]=counts[pt]
                        inv=True
            if amount>1000:
                inv=True

            if inv:
                resmap[transaction]=counts[transaction]


            mp[name].append([time,amount,city])
        
        for result in resmap:
            print(result, resmap[result])
            for i in range(resmap[result]):
                res.append(result)
        
        return res

