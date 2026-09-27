class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(0, len(nums), 1):
            difference = target - nums[i]

            if difference in nums_map:
                return [nums_map[difference], i]
            else:
                nums_map[nums[i]] = i