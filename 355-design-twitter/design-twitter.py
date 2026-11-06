import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap, (-time, tweetId, uid, index)
                )

        result = []

        while heap and len(result) < 10:
            negTime, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)

            if index > 0:
                index -= 1
                time, nextTweet = self.tweets[uid][index]

                heapq.heappush(
                    heap, (-time, nextTweet, uid, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)