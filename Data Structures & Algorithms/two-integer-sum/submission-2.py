class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        req = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in req:
                return [req[need], i]

            req[num] = i

        