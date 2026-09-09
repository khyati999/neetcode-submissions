class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid]<nums[right]:
                right=mid   # min is on left
            else:
                left = mid+1    # min is on the right
        return nums[left]