class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        for c in t:
            if c not in freq:
                return False
            freq[c] -= 1

        for k, v in freq.items():
            if v != 0:
                return False
        
        return True
        