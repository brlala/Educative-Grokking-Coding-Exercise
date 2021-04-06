import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = []
        self.num_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_map:
            return False
        self.num_map[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_map:
            return False
        last_elem_in_list = self.num_list[-1]
        index_to_remove = self.num_map[val]

        # switch element to remove to last position and update location
        self.num_list[index_to_remove], self.num_list[-1] = self.num_list[-1], self.num_list[index_to_remove]
        self.num_map[last_elem_in_list] = index_to_remove

        # remove from both data
        self.num_list.pop()
        self.num_map.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.num_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()