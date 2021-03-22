# 225. Implement Stack using Queues

## Problem Statement

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

**Notes**:

- You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.

## Main Concept

**Time complexity of operations** - Implementing a stack with queues necessarily means that either the push or pop operation is going to take hit to its time complexity.

## Challenges

Not using two queues - Using two queues wastes space. Therefore, to be space efficient we should implement a solution as which only uses one queue.

## Solution Explained

We initialise one array where we will only perform standard queue operations i.e. we can only pop from and peek array[0] and push to the back of the array. Thus our array behaves like a queue.

- **push** - We push the given number to the back of the queue. Now for `size - 1`, where `size` is the size of the array after pushing the given element, we pop the front of the queue and push it to the tail of the queue. After performing these operations we have the desired stack behaviour from our queue.

![push algorithm](./225_stack_using_queues_push.png)

- **pop** - We pop the front of the queue which is also the top of the stack.

- **top** - We access queue[0] which is the top of the stack.

- **empty** - If the length of the queue data structure is zero then it returns `True`, else `False`.
