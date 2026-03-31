from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.userToPost = defaultdict(list)
        self.userToFollowers = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1  # more recent = smaller
        self.userToPost[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followers = self.userToFollowers[userId]
        
        # Include the user's own tweets
        for post in self.userToPost[userId]:
            heapq.heappush(heap, post)

        # Include each followee's tweets
        for followee in followers:
            for post in self.userToPost[followee]:
                heapq.heappush(heap, post)

        res = []
        while heap and len(res) < 10:
            _, tweet = heapq.heappop(heap)
            res.append(tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userToFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowers[followerId].discard(followeeId)
