# 19. Remove Nth Node From End of List

## Problem Statement

Given the head of a linked list, remove the nth node from the end of the list and return its head.

**Follow up:** Could you do this in one pass?

## Solution Explained

To solve this problem with one pass of the list we send a scout ahead to the n+1<sup>th</sup> node from the start. When the scout reaches its destination our `follow` pointer is at the `head` of the list. Therefore, there are `n` nodes between our two pointers.

We then increment both our pointers by one till `scout` reaches the end node of our list. At this point, our `follow` pointer will be at the n+1<sup>th</sup> node from the end of the list.

Now, it is a simple matter of changing pointers so that the n<sup>th</sup> node from the end of the list is no longer a part of the list.

If our scout becomes `None`, then it means that we have to delete the head node of the list. So, we just return `head.next`.
