class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        List = []
        for i in nums:
            if i in List:
                return True
            List.append(i)
        return False