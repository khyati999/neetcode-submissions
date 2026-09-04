class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA=0
        st=[]
        for ind, h in enumerate(heights):
            start=ind
            while st and st[-1][1]>h:
                index, height=st.pop()
                maxA=max(maxA, height*(ind-index))
                start=index
            st.append((start, h))
        
        for ind, h in st:
            maxA=max(maxA, h*(len(heights)-ind))
        return maxA
