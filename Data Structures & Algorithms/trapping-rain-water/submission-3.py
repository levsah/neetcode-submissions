class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftTallest, rightTallest = height[l], height[r]
        totalWater = 0

        while l < r:
            if leftTallest < rightTallest:
                l += 1
                leftTallest = max(leftTallest, height[l])
                totalWater += leftTallest - height[l]
            else:
                r -= 1
                rightTallest = max(rightTallest, height[r])
                totalWater += rightTallest - height[r]

        return totalWater
        