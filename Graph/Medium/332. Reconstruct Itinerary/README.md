# 332. Reconstruct Itinerary

## Problem Statement

You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

## Solution Explained

We do a modified dfs where we go deep into the graph even if a node has been visited once.

While constructing the graph we make sure to maintain the list of destinations in a lexically sorted manner as the question demands.

We keep travelling to the next destination till there is no next destination. When we cannot go anywhere from a destination we put it in our stack. Therefore, the stack holds our itinerary in the reverse order.
