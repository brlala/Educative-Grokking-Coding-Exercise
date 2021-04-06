class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import heapq
        counts = collections.defaultdict(int)
        for w in words:
            counts[w] += 1

        freqs = []
        for word, counter in counts.items():
            heapq.heappush(freqs, (Element(counter, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        res = []
        for _ in range(len(freqs)):
            # print(heapq.heappop(freqs)[1])
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]


