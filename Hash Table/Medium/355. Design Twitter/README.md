355. Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List < Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

## Solution Explained

We keep a track of the tweets made by each user, the timestamp of the tweet and the users followed by one user.

Data structures used are:

- Tweets Dictionary: This maps userId to an array of pairs of tweet priority and tweetId i.e. (tweet_number, tweetId)

- Follows Dictionary: This maps userId to a set of users followed by the user.

Global Variables:

- tweet_number: A timestamp which lets us track the chronology of each tweet. We use this to sort the tweets in the `getNewsFeed` function.
