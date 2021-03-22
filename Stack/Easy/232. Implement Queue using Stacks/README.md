# 232. Implement Queue using Stacks

## Problem Statement

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

**Notes**:

- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

**Follow-up**: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

## Main Concept

**Amortised Time Complexity** - Amortized time is the way to express the time complexity when an algorithm has the very bad time complexity only once in a while besides the time complexity that happens most of time.

## Solution Explained

We initialise two arrays `s1` and `s2`. We only perform standard stack operations on these arrays thus they are made to behave like stacks. A variable `front` is initialised as `None` to keep track of the front of the queue.

- **push** - The push operation is simple and has O(1) time complexity where we push the given element onto `s1`.

- **pop** - When popping we move the elements from `s1` to `s2` if `s2` is empty. This takes O(n) time. Once all the elements are in `s2`, it contains the elements of the queue in reverse order i.e. the top of `s2` is the front of our queue. If `s2` already has elements then we simply pop the top of `s2`.

- **peek** - We return the top of `s2` if it is not empty. Else we return `front`.

- **empty** - As both `s1` and `s2` jointly contain the elements of our queue we must check if both are empty.
