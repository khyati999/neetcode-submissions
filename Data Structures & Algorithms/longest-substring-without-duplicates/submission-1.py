class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastSeen={}
        left, maxlen=0, 0
        for rightInd, char in enumerate(s):
            if char in lastSeen and lastSeen[char]>=left:
                left=lastSeen[char]+1
            lastSeen[char]=rightInd
            maxlen=max(maxlen, rightInd-left+1)
        return maxlen
        