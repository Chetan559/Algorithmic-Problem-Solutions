class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_vol = 0
        # curr_vol = 0
        i, j = 0, len(height) -1

        while i < j:
            h = min(height[i], height[j])
            w = j - i
            # curr_vol = h * w
            max_vol = max(max_vol, h*w)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_vol