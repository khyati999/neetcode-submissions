class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap={}

        for ind, num in enumerate(nums):
            dif=target-num
            if dif in numMap:
                return [numMap[dif],ind]
            numMap[num]=ind