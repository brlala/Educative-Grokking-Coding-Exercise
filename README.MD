# Pattern sliding window template
```
    window_start = 0
    for window_end in range(len(arr)):
        ...
        ...
        ...
        window_start += 1
        ...
```

# Pattern two pointers
```
    left, right = 0, len(arr) - 1
    while left < right:
        ...
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
            ...
```

# Fast Slow pointer
```
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        ...
```

# Pattern Merge interval
```
    intervals.sort(key=lambda x: x.start)
    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for index, itv in enumerate(intervals[1:], 1):
        if itv.start <= end:  # overlapping
            end = max(itv.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = itv.start
            end = itv.end
    merged_intervals.append(Interval(start, end))
    ...
```

# Pattern Cyclic Sort
```
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] <- need to -1 if the array is 1 based
        # while value less than length, ignore those that are out of array length
        if nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    ...
```

# Pattern reversing linked list
```
    prev = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

previous is now the head, current is now the tail after traversal

Traversing linked list:
        while current is not None and i < k:
            previous = current
            current = current.next
```

# Binary tree BFS
1. use a double ended queue
2. get the level size
3. loop the level size
4. popleft node
5. append left and right node
```
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level_values = []
        for _ in range(level_size):
            current_node = queue.popleft()
            # add the value to the current values
            current_level_values.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            # insert the children of current node in the queue
            if current_node.right:
                queue.append(current_node.right)
        result.append(current_level_values)
    return result
```

# Binary Tree DFS
1. create a helper method
2. define a stop condition
3. else traverse left + right node
4. backtrack when going up recursive calls(example 1/5)/return a specific condition(example 2)

Advance: (refer example 6, 7)
1. what do you want to return when you reach the end (stop condition)
2. traverse left + right
3. what do you want to return when you leave a node
4. keep a global variable if needed
```
def find_paths(root, sum):
    all_paths = []
    find_paths_recursive(root, sum, [], all_paths)
    return all_paths


def find_paths_recursive(current_node: TreeNode, sum, current_path: list, all_paths: list):
    """
    Time: O(N)
    Space: O(N) worst case if tree is a linked list
    """
    if current_node is None:
        return None

    # add the current node to the path
    current_path.append(current_node.val)

    # if the current node is a leaf and its value is equal to the sum, save the current path
    if current_node.val == sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(current_node.left, sum - current_node.val, current_path, all_paths)
        # traverse the right sub-tree
        find_paths_recursive(current_node.right, sum - current_node.val, current_path, all_paths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack
    del current_path[-1]
```
```
def find_max_paths(root: TreeNode) -> int:
    """
    https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    :param root:
    :return:
    """
    max_path = float("-inf")  # placeholder to be updated

    def get_max_gain(current_node):
        nonlocal max_path  # This tells that max_path is not a local variable
        if current_node is None:
            return 0

        gain_on_left = max(get_max_gain(current_node.left), 0)  # Read the part important observations
        gain_on_right = max(get_max_gain(current_node.right), 0)  # Read the part important observations

        current_max_path = current_node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
        max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

        return current_node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

    get_max_gain(root)  # Starts the recursion chain
    return max_path
```
# Two Heap Problem
Python always uses min heap, so when putting into max heap you need to add `-`
1. choose one heap as main, add to max heap if num is smaller than biggest number in max heap
2. balance the heap
```
class MedianOfAStream:
    max_heap = []  # containing first half of numbers
    min_heap = []  # containing second half of numbers

    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # either both the heaps will have equal number of elements or max heap will have one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            # we have even numbers, take the middle of two elements
            return (-self.max_heap[0]+self.min_heap[0])/2

        # because max heap has one more element than the mean heap
        return -self.max_heap[0]
```

# Binary Search
1. set start and end
2. constantly iterating the middle while reducing the range of start and end
```
def binary_search(arr):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return mid

    # since start<= end, the final iteration will be start==end+1, we are not able to find hence the next big number
    # will just be start
    return start  # use end if it is to find the floor
```