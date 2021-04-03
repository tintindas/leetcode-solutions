# 49. Group Anagrams

## Problem Statement

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Main Concept

**Anagram Sorting** - When sorted anagrams return the same string.

## Solution Explained

We maintain a hashmap that maps the sorted version of the anagrams to a list of the anagrams themselves.

For each word in the given list we sort the word and if we have not seen the sorted word we initialise a mapping from the sorted word to a list of anagrams that when sorted return our key, i.e., the sorted word. If we have seen this sorted word before then we append the word being processed to the list which is pointed to by our sorted word.
