from random import randint


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.arr.append(val)
            self.pos[val] = len(self.arr) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            pos = self.pos[val]
            last = self.arr[-1]
            self.arr[pos], self.arr[-1] = self.arr[-1], self.arr[pos]
            self.arr.pop()
            self.pos[last] = pos
            self.pos.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = randint(0, len(self.arr) - 1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()