# Implement the class ProductOfNumbers that supports two methods:
#
# 1. add(int num)
#
# Adds the number num to the back of the current list of numbers.
# 2. getProduct(int k)
#
# Returns the product of the last k numbers in the current list.
# You can assume that always the current list has at least k numbers.
# At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.
class ProductOfNumbers:
    """
    https://leetcode.com/problems/product-of-the-last-k-numbers/discuss/514694/Python3-97-solution

#     1* 2 * 3 *4 *5
#     1 2 6 24 120 (cumulative product)
#     1 12 123 1234 12345 (visualized)
    if you want to get last two, just take 12345 // 123
    """

    def __init__(self):
        self.queue = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.queue = [1]
        else:
            self.queue.append(self.queue[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.queue):
            return 0
        return self.queue[-1] // self.queue[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)