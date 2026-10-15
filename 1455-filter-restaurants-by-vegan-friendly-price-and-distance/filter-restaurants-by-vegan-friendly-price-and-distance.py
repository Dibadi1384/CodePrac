from sortedcontainers import SortedDict
class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        rmap=SortedDict()
        res=[]
        

        for restaurant in restaurants:
            i,r,v,p,d=restaurant[0],restaurant[1],restaurant[2],restaurant[3],restaurant[4]
            if veganFriendly:
                if d<=maxDistance and v and p<=maxPrice:
                    if -r in rmap:
                        rmap[-r].append(i)
                    else:
                        rmap[-r]=[i]
            else:
                if d<=maxDistance and p<=maxPrice:
                    if -r in rmap:
                        rmap[-r].append(i)
                    else:
                        rmap[-r]=[i]

        for r in rmap:
            rmap[r].sort(reverse=True)
            for i in rmap[r]:
                res.append(i)
        return res



