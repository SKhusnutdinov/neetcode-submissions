class Twitter:

    def __init__(self):
        self.count = 0
        self.followHM = defaultdict(set)
        self.tweetHM = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetHM[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followHM[userId].add(userId)
        for followeeId in self.followHM[userId]:
            if followeeId in self.tweetHM:
                index = len(self.tweetHM[followeeId]) - 1
                count, tweetId = self.tweetHM[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetHM[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followHM[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followHM[followerId]:
            self.followHM[followerId].remove(followeeId)
