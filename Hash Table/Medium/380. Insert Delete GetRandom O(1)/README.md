# 380. Insert Delete GetRandom O(1)

## Problem Statement

Implement the RandomizedSet class:

- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

## Solution Explained

For O(1) random operation we need to be able to access the elements of the set by their index.

To achieve this we maintain a dictionary which maps the value to the position and an array of values.

Implementation:

- `insert`: We add the element to the array and also to the value to index mapping dictionary.

- `remove`: pop operations from the end of the array are O(1) and accessing elements in both dictionaries and arrays are O(1) too.

  So we find the index of the element to be deleted from our mapping, then we swap it with the last element in the array. We then delete the last index of the array. The final step is to update the mapping of the element which was at the last index before deleting in our dictionary and delete the mapping of the deleted element from the dictionary.

- `getRandom`: We get a random index in the range of (0, len(arr) - 1) and return the element at that index.
