# 6. ZigZag Conversion

## Problem Statement

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

`string convert(string s, int numRows);`

## Solution Explained

We traverse through the string and keep adding the current letter to the row that it should be in.

We keep a track of the direction and current row.

If the current row is `0` or `numRows-1` we switch direction. `row` is updated according to which direction we are going in.
