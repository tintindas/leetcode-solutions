Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![Pascal's Triangle](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

## Main Concept

**Dynamic Programming** - We only need the previous row of the triangle to calculate the next row. Therefore only one array needs to be maintained in memory for this problem.

## Solution Explained

This is the same solution as [118. Pascal's Triangle](https://github.com/tintindas/leetcode-solutions/tree/main/Array/Easy/118.%20Pascal's%20Triangle).

The only modification made to the program is to only keep track of the previous array of the triangle rather than using memory to store the entire triangle.
