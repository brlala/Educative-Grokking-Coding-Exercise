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

# BFS
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