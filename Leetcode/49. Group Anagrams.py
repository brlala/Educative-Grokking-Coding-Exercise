import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            a = tuple(sorted(s))
            res[a].append(s)
        return res.values()