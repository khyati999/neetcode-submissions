class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        st=[]
        for ind, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                stTemp, stInd=st.pop()
                ans[stInd]=ind-stInd
            st.append((temp, ind))
        return ans
        