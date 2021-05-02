from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        https://leetcode.com/problems/bulls-and-cows/discuss/839444/Python-Simple-solution-with-counters-explained
        """
        # count bulls
        bulls = 0
        for idx, c in enumerate(secret):
            if c == guess[idx]:
                bulls += 1
        # bulls = sum([x==y for x,y in zip(secret, guess)])

        # count cows by taking b+c - b
        S_counter = Counter(secret)
        G_counter = Counter(guess)
        bulls_and_cows = 0
        for k, v in S_counter.items():
            bulls_and_cows += min(S_counter[k], G_counter[k])
        # bulls_and_cows = sum([min(S_counter[elem], G_counter[elem]) for elem in S_counter])
        return f"{bulls}A{bulls_and_cows - bulls}B"
