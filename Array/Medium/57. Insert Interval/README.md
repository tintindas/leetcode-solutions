# 57. Insert Interval

## Problem Statement

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

## Solution Explained

We look at each interval in the array.

If the end of the interval is less than the start of the interval to be inserted i.e. the entire interval is before our area of interest then we put them in a `left` array.

Similarly intervals which do not overlap our area of interest and are to the right of the area of interest are put in a `right` array.

When we encounter a interval which overlaps with our range of interest we take the minimum of the start of our range of interest and the start of the encountered interval and the maximum of the range of interest and the encountered interval. This merges intervals till we encounter an interval that does not overlap with our range of interest.
