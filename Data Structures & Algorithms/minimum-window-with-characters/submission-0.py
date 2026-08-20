class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window={}, {}
        for ch in t:
            countT[ch]=1+countT.get(ch, 0)
            
        have, need=0, len(countT)
        left=0
        res, resLen=[-1, -1], float("infinity")
        for right in range(len(s)):
            ch=s[right]
            window[ch]=1+window.get(ch, 0)
            if ch in countT and window[ch]==countT[ch]:
                have+=1
            while have==need:
                if (right-left+1)<resLen:
                    res=[left, right]
                    resLen=(right-left+1)
                    
                window[s[left]]-=1
                if s[left] in countT and window[s[left]]<countT[s[left]]:
                    have-=1
                left+=1
        left, right=res
        return s[left:right+1] if resLen!=float("infinity") else ""

        