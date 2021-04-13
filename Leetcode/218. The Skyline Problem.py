class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(x, -height, right) for x, right, height in buildings]
        events += list({(right, 0, None) for _, right, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float(inf))]
        for pos, negH, right in events:
            # 1, pop buildings that are already ended
            while pos >= live[0][1]:
                heappop(live)
            # 2, if it's the start-building event, make the building alive
            if negH:
                heappush(live, (negH, right))
            # 3, if previous keypoint height != current highest height, edit the result
            if res[-1][1] != -live[0][0]:
                res += [[pos, -live[0][0]]]
        return res[1:]




