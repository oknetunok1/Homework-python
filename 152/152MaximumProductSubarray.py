class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for x in nums[1:]:
            cur_max, cur_min = (
                max(x, x * cur_max, x * cur_min),
                min(x, x * cur_max, x * cur_min),
            )
            res = max(res, cur_max)
        return res