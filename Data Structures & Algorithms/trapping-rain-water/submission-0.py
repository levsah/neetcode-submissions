class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        tallestLeft, tallestRight = height[l], height[r]
        
        totalWater = 0

        while l < r:
            if tallestLeft < tallestRight: 
                l += 1
                tallestLeft = max(tallestLeft, height[l])
                totalWater += tallestLeft - height[l]
            else: 
                r -= 1
                tallestRight = max(tallestRight, height[r])
                totalWater += tallestRight - height[r]
        return totalWater

        