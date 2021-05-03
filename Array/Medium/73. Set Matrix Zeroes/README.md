# 73. Set Matrix Zeroes

## Problem Statement

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

## Solution Explained

- We iterate over the matrix and we mark the first cell of a row i and first cell of a column j, if the condition in the pseudo code above is satisfied. i.e. if cell[i][j] == 0.

- The first cell of row and column for the first row and first column is the same i.e. cell[0][0]. Hence, we use an additional variable to tell us if the first column had been marked or not and the cell[0][0] would be used to tell the same for the first row.

- Now, we iterate over the original matrix starting from second row and second column i.e. matrix[1][1] onwards. For every cell we check if the row r or column c had been marked earlier by checking the respective first row cell or first column cell. If any of them was marked, we set the value in the cell to 0.

- We then check if cell[0][0] == 0, if this is the case, we mark the first row as zero.

- And finally, we check if the first column was marked, we make all entries in it as zeros.
