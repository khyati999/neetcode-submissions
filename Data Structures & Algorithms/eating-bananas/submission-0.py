class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right=1, max(piles)
        res=right

        while left<=right:
            mid=(left+right)//2

            totTime=0
            for p in piles:
                totTime+=math.ceil(float(p)/mid)
            if totTime<=h:
                res=mid
                right=mid-1
            else:
                left=mid+1
        return res