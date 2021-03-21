# 155. Min Stack

## Problem Statement

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

- MinStack() initializes the stack object.
- void push(val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

## Main Concept

**Using Multiple Stacks** - To add the get minimum function to the stack data structure we must maintain two stacks. One which is the stack itself and the second, a stack of all the minimum elements inserted into the stack at the time of insertion

## Solution Explained

Our class has two attributes `stack` and `min_stack`

- `stack` is used to keep track of all push and pop operations.
- `min_stack` is used to implement the additional `getMin` functionality as it always keeps track of the minimum element inserted into the stack at the time of insertion i.e. top of the `min_stack` is always the minimum element inserted into the `stack`.

We only need to modify the `push` and `pop` operations to fulfill the requirements of the problem.

- `push` - When pushing we check if the number being pushed is less than or equal to the top of the `min_stack`, if it is then it is pushed to both the `stack` and the `min_stack`, if not then it is only pushed onto the `stack`.

- `pop` - The pop operation only needs to check if the top elements of both the stacks are equal. If they are then they are both popped. If not, then only the top of `stack` is popped.
