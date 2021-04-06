class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        import heapq
        task_frequency = collections.defaultdict(int)
        # add all tasks to the max heap
        for t in tasks:
            task_frequency[t] += 1

        max_heap = []
        for task, frequency in task_frequency.items():
            heapq.heappush(max_heap, (-frequency, task))

        interval_count = 0
        while max_heap:
            wait_list = []
            k = n + 1  # try to execute as many as 'k+1' tasks from the max-heap
            while k > 0 and max_heap:
                interval_count += 1
                frequency, task = heappop(max_heap)
                k -= 1
                if -frequency > 1:
                    # decrement the frequency and add to the waitList
                    wait_list.append((frequency + 1, task))

            # put all the waiting list back on the heap
            for frequency, task in wait_list:
                heapq.heappush(max_heap, (frequency, task))

            if max_heap:  # we'll be having 'n' idle intervals for the next iteration
                interval_count += k
        return interval_count
