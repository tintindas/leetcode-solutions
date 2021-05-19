# 447. Number of Boomerangs

## Problem Statement

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

## Solution Explained

We iterate over all possible pairs of the points. We get the euclidean distance for each pair of points. We keep a track of how many times a distance has appeared for the outer loop.

If the distance already exists in our dictionary we know that there are 2\*(number of times the distance has appeared) number of triplets that can be formed. (because order matters)
