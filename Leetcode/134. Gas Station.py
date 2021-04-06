class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Complexity n^2
        """
        if not gas or not cost or sum(cost) > sum(gas):
            return -1

        n = len(gas)
        for i in range(n):
            position = i
            balance = 0
            for _ in range(n):
                balance += gas[position % n] - cost[position % n]
                if balance < 0:
                    break
                position += 1
            else:
                return i
        return -1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        greedy algorithm
        """
        if not gas or not cost or sum(cost) > sum(gas):
            return -1
        position = balance = 0
        for i in range(len(gas)):
            balance += gas[i] - cost[i]
            if balance < 0:
                balance = 0
                position = i + 1
        return position

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        greedy algorithm without predicate
        """
        n = len(gas)
        position = balance = 0

        for i in range(2 * n):
            balance += gas[i % n] - cost[i % n]
            if balance < 0:
                balance = 0
                position = i + 1
        if position >= n:
            return -1
        return position


a = Solution()
a.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
