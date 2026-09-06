class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols= len(matrix), len(matrix[0])
        top, bot=0, rows*cols-1
        while top<=bot:
            mid=top+(bot-top)//2
            r, c=mid//cols, mid%cols
            if target>matrix[r][c]:
                top=mid+1
            elif target<matrix[r][c]:
                bot=mid-1
            else:
                return True
        return False