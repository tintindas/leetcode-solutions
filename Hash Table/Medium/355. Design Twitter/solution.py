from typing import List


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.follows = {}
        self.tweet_number = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweet_number += 1
        if userId in self.tweets:
            self.tweets[userId].append((self.tweet_number, tweetId))
        else:
            self.tweets[userId] = [(self.tweet_number, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []

        if userId in self.tweets:
            tweets.extend(self.tweets[userId])

        if userId in self.follows:
            for user in self.follows[userId]:
                if user in self.tweets:
                    tweets.extend(self.tweets[user])

        tweets.sort(reverse=True)
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            if followerId in self.follows:
                self.follows[followerId].add(followeeId)
            else:
                self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)