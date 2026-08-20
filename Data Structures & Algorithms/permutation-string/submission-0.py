class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1: # Count charecters in s1
            count1[ord(ch) - ord('a')] += 1
        
        window = len(s1)

        for i in range(window):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(window, len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1 
            
            count2[ord(s2[i - window]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False
