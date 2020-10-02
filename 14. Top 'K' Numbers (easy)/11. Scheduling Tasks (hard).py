# Problem Statement
# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.


def schedule_tasks(work_tasks, k):
    """
    Time: O(N*logN)
    Space: O(N)
    """
    from collections import defaultdict
    task_frequency = defaultdict(int)
    for task in work_tasks:
        task_frequency[task] += 1

    from heapq import heappop, heappush
    max_heap = []
    # add all tasks to the max heap
    for task, frequency in task_frequency.items():
        heappush(max_heap, (-frequency, task))

    interval_count = 0
    while max_heap:
        wait_list = []
        n = k + 1  # try to execute as many as 'k+1' tasks from the max-heap
        while n > 0 and max_heap:
            interval_count += 1
            frequency, char = heappop(max_heap)
            if -frequency > 1:
                # decrement the frequency and add to the waitList
                wait_list.append((frequency + 1, char))
            n -= 1

        # put all the waiting list back on the heap
        for frequency, char in wait_list:
            heappush(max_heap, (frequency, char))

        if max_heap:
            interval_count += n  # we'll be having 'n' idle intervals for the next iteration
    return interval_count


def main():
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " + str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
