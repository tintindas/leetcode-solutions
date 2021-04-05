# 187. Repeated DNA Sequences

## Problem Statement

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

- For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

## Solution Explained

We iterate over the given string storing the count of each "10 letter long" string in a hashmap. We return those elements of our hashmap which have values greater than 1.
