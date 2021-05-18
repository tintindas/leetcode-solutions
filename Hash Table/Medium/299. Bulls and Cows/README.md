# 299. Bulls and Cows

## Problem Statement

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

    The number of "bulls", which are digits in the guess that are in the correct position.
    The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

## Solution Explained

We count all the bulls first. Everything that is not a bull must then either be a cow or not.

We keep a count of all the non-bull characters from the `secret`. We also keep a track of all the non-bull characters from `guess`.

We iterate through all the non-bull characters from `guess` and every time we see a character which exists in our `count` map we decrease its count and add one to our `cow` count. If any character count reaches zero we remove it from our mapping.
