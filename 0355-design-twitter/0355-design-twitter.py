class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0 
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        relevant = self.following[userId] | {userId}
        heap = []
        for uid in relevant:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t,tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t , tid , uid, idx))
        feed = []
        while heap and len(feed) < 10:
                t, tid, uid, idx = heapq.heappop(heap)
                feed.append(tid)

                if idx > 0 :
                    idx -= 1
                    t2, tid2 = self.tweets[uid][idx]
                    heapq.heappush(heap, (-t2, tid2, uid, idx))

        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)