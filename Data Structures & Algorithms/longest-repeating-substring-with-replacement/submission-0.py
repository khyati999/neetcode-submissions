class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mpCount={}
        ans, left=0, 0
        maxFreq=0
        for right in range(len(s)):
            mpCount[s[right]]=1+mpCount.get(s[right], 0)
            maxFreq=max(maxFreq, mpCount[s[right]])
            while(right-left+1)-maxFreq>k:
                mpCount[s[left]]-=1
                left+=1
            ans=max(ans, right-left+1)
        return ans
        

        